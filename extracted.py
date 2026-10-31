
import os
folder_path = "documents"
documents = []
if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    for filename in files:

        if filename.endswith(".txt"):

            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:

                content = file.read()

               
                documents.append({
                    "filename": filename,
                    "content": content
                })

    print("DOCUMENT LOADER ")

    for i, doc in enumerate(documents, start=1):
        print("\nDocument:", i)
        print("Filename:", doc["filename"])
        print("Content:", doc["content"])
    print("Total Documents Loaded:", len(documents))
    print("Document Loading Completed Successfully!")

else:
    print("Documents folder does not exist!")
file_path = "documents/python.txt"

with open(file_path, "r", encoding="utf-8") as file:
    extracted_text = file.read()

print("Extracted Text:")
print(extracted_text)
