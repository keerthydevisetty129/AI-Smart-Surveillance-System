print("AI Smart Surveillance System")

print("1 - Object Detection")
print("2 - Vehicle Counting")
print("3 - Phone Detection")
print("4 - Helmet Detection")

choice = input("Select option: ")

if choice == "1":
    import src.object_detection

elif choice == "2":
    import src.vehicle_counter

elif choice == "3":
    import src.phone_detection

elif choice == "4":
    import src.helmet_detection

else:
    print("Invalid option")