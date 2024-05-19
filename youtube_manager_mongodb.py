
import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["database_name"]

video_collection = db["videos"]



def list_All():
    for video in video_collection.find():
        print(f"ID: {video._id}, Title: {video["name"]},Time:{video["time"]}")


def add_video():
    video_collection.insert_one({"name":"Jhaz","time":"2015-78-8"})


def update_video():
    video_collection.update_one({"name":"Jhaz"},{"$set":{"name":"Jhaz-updated","time":"456543edfv"}})


def delete_video():
    video_collection.delete_one({"name":"Jhaz"})


def main():
    while True:
        print("youtube manager | mongodb")
        
        print("1 - List All videos")
        print("2 - Add videos")
        print("3 - Update videos")
        print("4 - Delete videos")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            list_All()
        elif choice == "2":
            add_video("video 1","time 4")
        elif choice == "3":
            update_video(1,"video 2","time")
        else:
            delete_video(1)
            
            
        


if __name__ == "__main__":
    main()