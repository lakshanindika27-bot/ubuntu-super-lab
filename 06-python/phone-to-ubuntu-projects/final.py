# ubuntu-super-lab - 06-python - Final - All 7 Types

# 1. string
name = "Laksh"
lab = "ubuntu-super-lab"
print(f"Name: {name}, Lab: {lab} - Type: {type(name)}")

# 2. tuple
version = (1, 0, "stable")
print(f"Version: {version} - Type: {type(version)}")

# 3. list
labs = ["01-foundation", "06-python", "13-mlops"]
print(f"Labs: {labs} - Type: {type(labs)}")

# 4. dict
status = {"06-python": "doing", "13-mlops": "dream"}
print(f"Status: {status} - Type: {type(status)}")

# 5. integer
total = 15
print(f"Total Labs: {total} - Type: {type(total)}")

# 6. boolean
is_laptop = True
print(f"Is Laptop? {is_laptop} - Type: {type(is_laptop)}")

# 7. float 
accuracy = 0.9234
loss = 0.0742
progress = 6/15*100
print(f"\n=== FLOAT - HEART OF AI ===")
print(f"Accuracy: {accuracy} -> {accuracy*100:.2f}%")
print(f"Loss: {loss}")
print(f"Progress: {progress:.2f}%")
print(f"Type: {type(accuracy)}")

if accuracy > 0.9:
    print("-> Ready for 13-mlops!")
