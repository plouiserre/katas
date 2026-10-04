def get_player(players, first_letter): 
        player_name = ""
        for player in players : 
            first_letter_player = player[0:1]
            if first_letter == first_letter_player : 
                player_name = player
                break
        return player_name