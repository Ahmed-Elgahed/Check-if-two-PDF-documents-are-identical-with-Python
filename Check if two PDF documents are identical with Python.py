import hashlib

def hash_file(filename1, filename2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(filename1, "rb") as file:
        chunk = file.read(1024)
        while chunk:
            h1.update(chunk)
            chunk = file.read(1024)

    with open(filename2, "rb") as file:
        chunk = file.read(1024)
        while chunk:
            h2.update(chunk)
            chunk = file.read(1024)

    return h1.hexdigest(), h2.hexdigest()


file1 = r"C:\Users\ASUS\Downloads\Coursera IIIF4ZKP7RS7.pdf"
file2 = r"C:\Users\ASUS\Downloads\Coursera JS68OUHZFF9P.pdf"

msg1, msg2 = hash_file(file1, file2)

if msg1 != msg2:
    print("these files are not identical")
else:
    print("these files are identical")