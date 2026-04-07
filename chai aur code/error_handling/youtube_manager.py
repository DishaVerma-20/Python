import json

def load_data():
    try:
        with open ('youtube.txt') as file:
            test = json.load(file)
            print(type(test))
            return test
    except:
        return []
    
def save_data_helper(videos):
    with open ('youtube.txt', "w") as file:
        json.dump(videos, file) # saara data write kar dete haii

def list_all_videos(videos):
    print("\n")
    print('*' * 70)
    # for index, video in enumerate(videos, start = 1):
    # for vid in videos:
    #     print(f"{videos}")
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print('*' * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time ")
    videos.append({"name": name, "time" : time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Successfully deleted")
    else:
        print("Invalid video index selected..")

videos = load_data() # file se data fetch, agar file mai nahi hai toh khali parenthesis 

def main():
    while True:
        print("\n YouTube Manager | Choose an option")
        print("1. List all the youtube videos")
        print("2. Add a youtube video")
        print("3. Update details of a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)

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