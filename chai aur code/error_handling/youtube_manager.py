def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

videos = []

def main():
    while True:
        print("\n YouTube Manager | Choose an option")
        print("1. List all the youtube videos")
        print("2. Add a youtube video")
        print("3. Update details of a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        # multiple cases evaluate krke match krti haii
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _: # baaki saari chije cover ho jaygi apne aap
                print("Invalid choice!")
            
if __name__ == "__main__":
    main()
    # Code sirf tab chale jab file directly run ho, import hone par nahi