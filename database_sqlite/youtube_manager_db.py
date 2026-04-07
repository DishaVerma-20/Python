import sqlite3
con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    pass

def add_video():
    pass

def update_video():
    pass

def delete_video():
    pass

def main():
    while True:
        print("\n YouTube manager app with DB")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit from the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter time of video: ")
            add_video(name, time)
        elif choice == '3':
            id = input("Enter video ID to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(id, name, time)

        elif choice == '4':
            id = input("Enter video ID to be deleted: ")
            delete_video(id)
            print("Successfully deleted!")
        
        elif choice == '5':
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

