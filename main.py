from engine.inference import Inference

# # for disease inference
knowledgeBaseFile = "./data/diseases/knowledge.json"
clauseBaseFile = "./data/diseases/clause.json"

inferenceEngine = Inference()
inferenceEngine.startEngine(knowledgeBaseFile,
                            clauseBaseFile,
                            verbose=True,
                            method=inferenceEngine.BACKWARD)
