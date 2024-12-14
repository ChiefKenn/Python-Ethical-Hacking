import datetime

def write_log(file_path, message) :
    """Function that appends logs to a file with time stamp"""
try :
    with open(file_path, "a") as file:
        timestamp =  datetime.datetime.now().strftime("%Y - %m- %d - %H: %M: %S") 
        file.write(f"{timestamp} + {message} \n") 
    print( f"log:{message}" )
except Exception as e:
    print(f"error written log: {e}")


def read_log(file_path) :
        """function is meant to read content from the file"""
        try:
            with open(file_path, "r") as file:
                print(f" \n ----- log-------------------")
                for line in file:
                    print(line.strip())

        except FileNotFoundError:
                print("No logs found")
        except Exception as e:
            print(f"error written log {e}")

if __name__ == "__main__" :
     log_file = "filename.txt"
     while True:
        print("\n Log Manager Options")
        print("1 Wrirte log entry")
        print("2 Read all  log entry")
        print("3 Exit")

        choice = input("Select an option from the log manager: ")
        if choice == "1": 
            log_message = input("Enter your log message:")
            write_log(log_file, log_message)
            
        elif choice == "2":
            read_log(log_file)
        
        elif choice == "3":
            print("Exitting / Thanks for your time")
            break

        else:
            print("Invalid Option!")
