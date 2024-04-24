import os
import time
import joblib
import librosa
import numpy as np

SAVE_DIR_PATH = "C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/joblib_features"
TRAINING_FILES_PATH = "C:/Users/2/Documents/Speech Emotion Recognition Project/Final Speech Emotion Recognition Project/features"


class CreateFeatures:

    @staticmethod
    def features_creator(path, save_dir) -> str:
        lst = []

        start_time = time.time()

        for subdir, dirs, files in os.walk(path):
            for file in files:
                try:
                    X, sample_rate = librosa.load(os.path.join(subdir, file),
                                                  res_type='kaiser_fast')
                    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate,
                                                         n_mfcc=40).T, axis=0)
                    file = int(file[7:8]) - 1
                    arr = mfccs, file
                    lst.append(arr)

                except ValueError as err:
                    print(err)
                    continue

        print("--- Data loaded. Loading time: %s seconds ---" % (time.time() - start_time))

        X, y = zip(*lst)

        X, y = np.asarray(X), np.asarray(y)

        print(X.shape, y.shape)

        X_name, y_name = 'X.joblib', 'y.joblib'

        joblib.dump(X, os.path.join(save_dir, X_name))
        joblib.dump(y, os.path.join(save_dir, y_name))

        return "Completed"


if __name__ == '__main__':
    print('Routine started')
    FEATURES = CreateFeatures.features_creator(path=TRAINING_FILES_PATH, save_dir=SAVE_DIR_PATH)
    print('Routine completed.')
