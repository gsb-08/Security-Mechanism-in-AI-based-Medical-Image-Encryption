import os

print("🔍 Searching for your NORMAL folder...\n")

# Search from data folder
base = "data"

def find_folders(path, target="NORMAL", depth=0, max_depth=5):
    """Recursively find folders"""
    if depth > max_depth:
        return
    
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            
            if os.path.isdir(item_path):
                # Print with indentation
                indent = "  " * depth
                print(f"{indent}📁 {item}/")
                
                # Check if this is the NORMAL folder
                if item == target:
                    # Count files inside
                    try:
                        files = [f for f in os.listdir(item_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
                        if len(files) > 0:
                            print(f"{indent}   ✅ FOUND IT! Contains {len(files)} images")
                            print(f"{indent}   👉 USE THIS PATH: {item_path}")
                            print()
                    except:
                        pass
                
                # Recurse into subdirectory
                find_folders(item_path, target, depth + 1, max_depth)
    except PermissionError:
        pass

find_folders(base)

print("\n" + "="*60)
print("Copy the path marked with 👉 into your explore_data.py file!")
print("="*60)