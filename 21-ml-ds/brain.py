# New Version:
# imageai.Prediction no longer exists, replaced by imageai.Classification
import os

from imageai.Classification import ImageClassification

exec_path = os.getcwd()
print(exec_path)

prediction = ImageClassification()
# SqueezeNet model also no longer exists, now the fastest is MobileNetV2
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path, "mobilenet_v2-b0353104.pth"))
prediction.loadModel()

# predictions, probabilities = prediction.classifyImage(os.path.join(exec_path, 'house.jpg'), result_count=5)
# predictions, probabilities = prediction.classifyImage(
#     os.path.join(exec_path, "pig.jpg"), result_count=5
# )
# for eachPred, eachProb in zip(predictions, probabilities):
#     print(f"{eachPred} : {eachProb}")

# predictions, probabilities = prediction.classifyImage(os.path.join(exec_path, 'house.jpg'), result_count=5)
for image_name in ["giraffe.jpg", "godzilla.jpg", "house.jpg", "pig.jpg"]:
    predictions, probabilities = prediction.classifyImage(
        os.path.join(exec_path, image_name), result_count=5
    )
    print("-" * 30)
    print(f"Results for {image_name}:")
    for eachPred, eachProb in zip(predictions, probabilities):
        print(f"{eachPred} : {eachProb}")
print("-" * 30)


# -------------
# Old Version:
# from imageai.Prediction import ImagePrediction
# import os
# execution_path=os.getcwd()
#
# prediction = ImagePrediction()
# prediction.setModelTypeAsSqueezeNet()
# prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
# prediction.loadModel()
#
# predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5 )
# for eachPrediction, eachProbability in zip(predictions, probabilities):
#     print(eachPrediction , " : " , eachProbability)
