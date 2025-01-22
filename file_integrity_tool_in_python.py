import hashlib
import json
import os 
import string


def new_hashes_saved(new_hashes,file_hash="file_hashes.json"):
    # Save the current hashes to a JSON file.
    with open(file_hash,'w') as new2:
        json.dump(new_hashes,new2)
    

def hash_calculation(file,algoritm="sha256"):
    """Calculate the hash of a given file using the specified algorithm."""
    new_hash_algorithm=hashlib.new(algoritm)
    try:
        with open(file,'rb') as new1:
             while chunk:= new1.read(8192):
                new_hash_algorithm.update(chunk)
        return new_hash_algorithm.hexdigest()
    except FileNotFoundError:
         print(f"File not found: {file}")
         return None



def hash_values_loader(file_hash="file_hashes.json"):
    """Load stored file hashes from a JSON file."""
    if os.path.exists(file_hash):
        try:
            with open(file_hash, 'r') as new3:
                return json.load(new3)
        except json.JSONDecodeError:
            print(f"Error: {file_hash} is corrupted or unreadable.")
    else:
        return {}
    


def File_monitoring(All_files,algorithm='sha256'):
    """Monitor files for changes based on their hash values."""
    current_hash={}
    stored_hash=hash_values_loader()
    for file in All_files:
        hash_file=hash_calculation(file,algorithm)
        if hash_file != None:
            current_hash[file]=hash_file
            if file in stored_hash:
                if stored_hash[file]==hash_file:
                    print(f"The file {file} is not having any changes")
                else:
                    print(f"The file {file} is having some changes")
            else:
                print(f"file {file} not found in the hashlib")
    new_hashes_saved(current_hash)
        

    


if __name__=="__main__":
    input_files = input("Enter file names separated by commas: ")
    All_files=[file.strip() for file in input_files.split(",")]
    File_monitoring(All_files)
