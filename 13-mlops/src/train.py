# 13-mlops - Real MLOps Pipeline - by Laksh
import random




# FLOATේ ජීවිතේ!
def train_model():
    print("=== MLOps Lab - Training Started ===")
    
    # Data (list + dict)
    datasets = ["ai-lab", "mlops-lab", "ubuntu-super-lab"]
    metrics = {}
    
    # Simulate Training - Float values
    for epoch in range(1, 4):
        accuracy = 0.80 + random.random() * 0.15  # 0.80 to 0.95
        loss = 1.0 - accuracy + random.uniform(0, 0.05)
        
        metrics[f"epoch_{epoch}"] = {
            "accuracy": round(accuracy, 4),
            "loss": round(loss, 4)
        }
        print(f"Epoch {epoch}: Accuracy={accuracy*100:.2f}% | Loss={loss:.4f}")

    # Final float
    final_accuracy = metrics["epoch_3"]["accuracy"]
    print(f"\nFinal Accuracy: {final_accuracy} -> {final_accuracy*100:.2f}%")
    
    if final_accuracy > 0.90:
        print("-> MODEL READY FOR PRODUCTION! 🚀")
    else:
        print("-> Need more training")

    # Save metrics (dict to file)
    with open("models/metrics.txt", "w") as f:
        f.write(str(metrics))
    
    return metrics

if __name__ == "__main__":
    train_model()
