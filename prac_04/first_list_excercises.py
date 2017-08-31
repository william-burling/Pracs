song_list_file = open("songs.csv")
song_list_data = song_list_file.readlines()

subjects = song_list_data[0].strip().split(",")
song_list_values = []
for song_list_line in song_list_data[1:]:
    song_list_strings = song_list_line.strip().split(",")
    song_list_numbers = [int(value) for value in song_list_strings]
    song_list_values.append(song_list_numbers)
song_list_file.close()
song_list_by_subject = reorganise_song_list_by_subject(song_list_values)
display_subject_details(songs_list_by_subject, subjects)

