import dropbox
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token


    def upload_file(self, folder_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        files = os.listdir(folder_from)
        for root,dirs,files in os.walk(file_from):
                relative_path = os.path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to. relative_path)
                with open(local_path,'rb') as f:
                     dbx.files_upload(f.read(), dropbox_path, mode=Writemode('overwrite'))
                     


def main():
    access_token = 'sl.Bhb8-BMdP8rDe4fZOyTDn1qyVzjCx0zwyoLOszqCvLkpQX-d758qhA1Zrkpmg8cD_gFI6ojStYBKyu1dB2zlKNE-SMqMnFG3_kAIRjuB7-AlCxpU6Nnyo7GMk4xKW1OmbQdDVnLK58WH'
    transferData = TransferData(access_token)


    file_from = input("Enter the full path of the file to be uploaded.")
    file_to = input("Enter the path of location in dropbox.")


    # API v2
    transferData.upload_file(file_from, file_to)


main()





