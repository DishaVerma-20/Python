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
    cursor.execute("SELECT * FROM videos") # yha se tuple aayga toh isliye loop lgana hoga
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO VIDEOS (name, time) VALUES (?, ?)",(name, time)) 
    # ye 2nd vala name time variable hai jo ques maek ko replace krege
    con.commit()

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,)) # ek trailing comma sa he tuple mai jayga, aur tuple he accept hota haii
    con.commit()

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

    con.close()

if __name__ == "__main__":
    main()

