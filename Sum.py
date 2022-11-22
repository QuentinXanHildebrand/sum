def main():

    f= open("meep.txt", "w")

    f.write("Mep mepp meep")
        
    f.close()

    f = open("meep.txt", "r")
    
    lines = f.read()
    
    print(lines)
    
    f.close()
    
main()