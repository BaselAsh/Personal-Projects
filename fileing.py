import os.path

def main():
    thePath = os.getcwd() + r"\paa.py"
    myFile = open(thePath, "w")
    myFile.write("print(\"Hello World\")\nprint(\"How Are You? :)\")")
    myFile.close()




if __name__ == "__main__":
    main() 
    
