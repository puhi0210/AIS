import weka.core.jvm as jvm
from weka.core.classes import Random
from weka.core.converters import Loader
from weka.classifiers import Classifier, Evaluation, PredictionOutput
from weka.core.dataset import Instance

jvm.start()

data_file = 'labVaje/vaja2/data/air_quality.arff'
loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file(data_file)
data.class_is_last()

# generate train/test split of randomized data
train, test = data.train_test_split(66.0, Random(1))



# build and train a classifier
cls = Classifier(classname="weka.classifiers.trees.J48")
cls.build_classifier(train)

print("=== J48 Classifier Structure ===")
print(cls)



# test the model
evl = Evaluation(train)
output = PredictionOutput(classname="weka.classifiers.evaluation.output.prediction.PlainText")

# Evaluate 
evl.test_model(cls, test, output=output)

accuracy = evl.percent_correct
print(f"\nAccuracy: ", accuracy, "%")
err = evl.percent_incorrect
print(f"\nError: ", err, "%")
print("\nConfusion Matrix:")
print(evl.confusion_matrix)



# find out current air quality in Celje
#         [PM2.5, PM10, O3, NO2, SO2]
current_aiq = [77, 27, 10, 12, 2]
inst = Instance.create_instance(current_aiq)
inst.dataset = data
index = cls.classify_instance(inst)
print("\nCurrent air qualty: ", inst.class_attribute.value(int(index)))


jvm.stop()