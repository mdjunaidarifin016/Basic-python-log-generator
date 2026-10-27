import logging
import os

logging.basicConfig(filename="app.log",filemode='a',format='%(asctime)s %(levelname)s %(name)s: %(message)s',datefmt="%Y-%m-%d %H:%M:%S")
logger=logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.INFO)

logger.info("Application start")
def menu():
    while True:
        print("======= LOG GENERATOR =======")
        print("1. Application started")
        print("2. User login")
        print("3. User logout")
        print("4. Warning event")
        print("5. Error event")
        print("6. Task completed")
        print("7. File opened")
        print("8. File not found")
        print("9. Exit")
        print("=============================")

        try:
            choice=int(input("Enter your choice:"))
        except ValueError:
            logger.warning("Enter a valid choice!(enter number not alphabet)")
            print("Enter a valid choice!(enter number not alphabet)")
            continue
        if choice==1 :
            logger.info("Application started")
        elif choice==2 :
            logger.info("User login")
        elif choice==3 :
            logger.info("User logout")
        elif choice==4 :
            logger.warning("Warning event")
        elif choice==5 :
            logger.error("Error event")
        elif choice==6:
            logger.info("Task completed")
        elif choice==7:
            logger.info("File opened")
        elif choice==8 :
            file_name=input("Enter the filename you want to open:")
            if not file_name.strip():
                logger.warning("filename not entered")
                print("file name not entered please enter a file name")
                continue
            else:
                try:
                    with open (file_name,"r")as f :
                        data=f.read()
                        logger.info(f"{file_name} file opened")
                        print(data)
                except FileNotFoundError:
                    logger.exception(f"Failed to open {file_name} file")
        elif choice==9 :
            print("Good bye!")
            logger.info("Application close!")
            break
        else:
            logger.warning("Enter a valid choice!(enter number from 1 to 9)")
            print("Enter a valid choice!(enter number from 1 to 9)")
menu()