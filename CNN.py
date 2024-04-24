import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.layers import Conv1D
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Activation
from keras.models import Sequential
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


SAVE_DIR_PATH = "C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/joblib_features"
MODEL_DIR_PATH = "C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project"


class TrainModel:

    @staticmethod
    def train_neural_network(X, y) -> None:

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        x_traincnn = np.expand_dims(X_train, axis=2)
        x_testcnn = np.expand_dims(X_test, axis=2)

        print(x_traincnn.shape, x_testcnn.shape)

        model = Sequential()
        model.add(Conv1D(64, 5, padding='same',
                         input_shape=(40, 1)))
        model.add(Activation('relu'))
        model.add(Dropout(0.2))
        model.add(Flatten())
        model.add(Dense(8))
        model.add(Activation('softmax'))

        print(model.summary)

        model.compile(loss='sparse_categorical_crossentropy',
                      optimizer='rmsprop',
                      metrics=['accuracy'])

        cnn_history = model.fit(x_traincnn, y_train,
                               batch_size=16, epochs=50,
                               validation_data=(x_testcnn, y_test))

        plt.plot(cnn_history.history['loss'])
        plt.plot(cnn_history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        loss_plot_path = "C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/Images/loss.png"
        plt.savefig(loss_plot_path)
        plt.close()

        plt.plot(cnn_history.history['accuracy'])
        plt.plot(cnn_history.history['val_accuracy'])
        plt.title('model accuracy')
        plt.ylabel('acc')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        accuracy_plot_path = "C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/Images/accuracy.png"
        plt.savefig(accuracy_plot_path)

        predictions = model.predict_classes(x_testcnn)
        new_y_test = y_test.astype(int)
        matrix = confusion_matrix(new_y_test, predictions)

        print(classification_report(new_y_test, predictions))
        print(matrix)

        model_name = 'Speech Emotion Recognition.h5'

        if not os.path.isdir(MODEL_DIR_PATH):
            os.makedirs(MODEL_DIR_PATH)
        model_path = os.path.join(MODEL_DIR_PATH, model_name)
        model.save(model_path)
        print('Saved trained model at %s ' % model_path)


if __name__ == '__main__':
    print('Training started')
    X = joblib.load(SAVE_DIR_PATH + '\\X.joblib')
    y = joblib.load(SAVE_DIR_PATH + '\\y.joblib')
    NEURAL_NET = TrainModel.train_neural_network(X=X, y=y)
