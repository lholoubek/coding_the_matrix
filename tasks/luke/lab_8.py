import numpy as np
import os

TRAINING_DATA = "train.data"
VALIDATION_DATA = "validate.data"

class PatientDataSet(object):
    def __init__(self, data=None):
        self.patient_ids = set()
        self.data = None
        self.labels = None
        if data:
            self.load_cancer_data(data)

    def load_cancer_data(self, file_name):
        # loads cancer data from filename
        # returns {"data":matrix with rows as features, "labels":vector}

        if not os.path.exists(file_name):
            raise FileExistsError("Provided data file doesn't exist")
        params = ["radius", "texture", "perimeter","area","smoothness","compactness","concavity","concave points","symmetry","fractal dimension"];
        stats = ["mean", "stderr", "worst"]
        columns = [param + "_" + stat for param in params for stat in stats]
        rows = []
        labels = []
        patient_ids = set()
        with open(file_name) as data_file:
            for line in data_file.readlines():
                cleaned = line.strip()
                row = cleaned.split(",")
                self.patient_ids.add(row[0])
                labels.append(-1 if row[1]=="B" else 1)
                rows.append([float(item) for item in row[2:]])
        self.data = np.array(rows)
        self.labels = np.array(labels)

class Weights(object):
    def __init__(self, vec):
        self.vec = vec

    @staticmethod
    def signum(vec):
        one_neg_one = lambda x: 1 if x >= 0 else -1 
        signum_vec = np.array([one_neg_one(x) for x in vec])
        return signum_vec

    def evaluate(self, data_set):
        assert self.vec.shape[0] == data_set.data.shape[1]
        predictions = data_set.data.dot(self.vec)
        signum_predictions = Weights.signum(predictions)
        delta = signum_predictions - data_set.labels
        halved = .5 * delta
        total_wrong = halved.dot(halved)
        percent_wrong = total_wrong/len(data_set.labels)
        return percent_wrong
    
    def loss(self, data_set):
        predictions = data_set.data.dot(self.vec)
        signum_predictions = Weights.signum(predictions)
        delta = data_set.labels - signum_predictions
        return delta.dot(delta)

    def find_gradient(self, data_set):
        predictions = data_set.data.dot(self.vec)
        signum_predictions = Weights.signum(predictions)
        less_b = signum_predictions - data_set.labels
        two_less_b = 2 * less_b
        gradient = np.transpose(data_set.data).dot(two_less_b)
        return gradient
    
    def report(self, data_set, training_iteration=None):
        print("Reporting performance")
        if training_iteration:
            print("Training iteration {}...".format(training_iteration))
        print("Loss: {}".format(self.loss(data_set)))
        print("Percent wrong: {}\n".format(self.evaluate(data_set)))

    def train(self, iterations, step_size, data_set):
        for i in range(iterations):
            gradient = self.find_gradient(data_set)
            adjustment = step_size * gradient
            self.vec = self.vec - adjustment
            if i % 3000 == 0:
                self.report(data_set, training_iteration=i)
        print("Training complete. Final weights: ")
        print(self.vec)

    def __repr__(self):
        return self.vec.__repr__()

if __name__ == "__main__":
    training_data = PatientDataSet(TRAINING_DATA)
    validation_data = PatientDataSet(VALIDATION_DATA)
    test = np.ones((training_data.data.shape[1]), dtype='float')
    weights = Weights(test)
    weights.train(100000, 0.01, training_data)
    print("Performance on validation data: ")
    weights.report(validation_data)
