#Return contextual giphy image URL based on proejct size
import streamlit as st


def Giphy_Size_Selector(Size):
    import random
    import re
    if Size == "Small":
        small_image_list = [
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExN29rMXp0bjJ4cWdyOWZtbTYxdzVya3VvejMwbTJ6dnJldWxlOWEwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oO8Io8e7uHu8gJQYbg/giphy.webp",
        "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExanM4NWEwd3dnbzQ5Y3NmY3lhdTZlejBkYnByaTV1NzBrazlxenpybCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9Vvbfc81jq94lsEgZU/giphy.webp",
        "https://media2.giphy.com/media/45dTbxpwjAPnEvDgWv/giphy.webp?cid=ecf05e477ge38cajtq6mypeiyg2s6k6gieaqereugi33zfiy&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media2.giphy.com/media/MytrrwDeFkQq1sDH97/giphy.webp?cid=ecf05e47g7g15tt0ovopha431di9ogwxo1qc648f79u7duhh&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media4.giphy.com/media/eCtjGnpxczc11MFunw/200.webp?cid=ecf05e479hmhf2sx61aby9qpufw068burntzzcd9ramx6j3j&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media4.giphy.com/media/km2mais9qzYI/giphy.webp?cid=790b7611v22jq8811kvunxc7djl41pnt4m4mww3uwyk7xsiu&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media2.giphy.com/media/cMJHOY2jGEHn2L48PC/giphy.webp?cid=ecf05e47smx4scw2o14tuwyb45d0afycw006y0l2xxh1vzso&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media1.giphy.com/media/TkXu7KNtU3pLO/giphy.webp?cid=ecf05e47k0tymyffl73uenhfucq7lx5smptrnaycgq0v81ip&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media0.giphy.com/media/3oeSB4QO7xBfFNqnKw/100.webp?cid=790b761140uefffllf4xytt50jcz88w3o63jv5mcmhmt96qw&ep=v1_gifs_search&rid=100.webp&ct=g",
        "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHR5bGtzamlsODhydXg2MzdsNDV0M3N0dHBzZ3NtcXVsN3A5MmJ3MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l41K1KTfqf2VGjyiQ/200.webp"
        ]
        return random.choice(small_image_list)
    if Size == "Medium":
        medium_image_list = [
        "https://media3.giphy.com/media/v5WZ2uwiW4VcVay8Sw/200.webp?cid=790b7611btldgosk6reine9ccqw42xs2cbdmgqyja8eolinh&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnRsZGdvc2s2cmVpbmU5Y2NxdzQyeHMyY2JkbWdxeWphOGVvbGluaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/7qfo1V3gIOOs0/200.webp",
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWM2MHlvNGVmc2hvbDQycWF2NGllOHd0cW9pczl4NzNwcDg5Z2V6diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XCct4Twj5bx48HXtZU/giphy.webp",
        "https://media4.giphy.com/media/JsKiYLRzEjpyo/200.webp?cid=ecf05e476cfrh0vb78rvhheuvriwfn0qe8pvbkhxq8zyk3ec&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media2.giphy.com/media/fyitaOqckoJX9k9tf2/200w.webp?cid=ecf05e47fm4nyi70ovgn1jqanudbtekb95oipy4k2kjuzomj&ep=v1_gifs_related&rid=200w.webp&ct=g",
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXV5emN5dHp5ejE3eHdvcDU5eGFnOXFiZXV0bHdydWhvNnM3bDJuMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YaLyGY3YILpxfjdJFD/200w.webp",
        "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDBjcXEzaXc1cDZhbG1nNzFvNTdieXN5aGdzemh6aHFjbjU0MW5xdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/gAap1hEomkx2cktXYT/200.webp",
        ]
        return random.choice(medium_image_list)
    if Size == "Large":
        large_image_list = [
        "https://media1.giphy.com/media/Xb761qMMBKPEPsxlgu/giphy.webp?cid=ecf05e47xiqwu2vi4s7jazei9tbufmg8xlltvkoek99y9lr1&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media3.giphy.com/media/raBbE1fizfZGE/200.webp?cid=ecf05e47xiqwu2vi4s7jazei9tbufmg8xlltvkoek99y9lr1&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media0.giphy.com/media/l2YWuU2n6lYHtLHEI/200.webp?cid=790b7611lci60410wm8qsic0kkjpf6v9equhlpvofsrtlpok&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media3.giphy.com/media/If9DvbHHowI1SWKLae/giphy.webp?cid=ecf05e47dtl4f5nmxanmspsqiam8xhhm8mpnsk4cgkbuzakd&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media0.giphy.com/media/l3q2Lz5yuEFUXX3IQ/giphy.webp?cid=790b7611h8nw1howj6uay4imgh0or7ebh2lb3x76fsnfvjuh&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGJrcmduOGw5cnljcDJ0Nmh0b2VrMHp4Y3FpdTZhcjlkbGZibDVkaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LpkBAUDg53FI8xLmg1/200.webp",
        "https://media0.giphy.com/media/O0cnJyVbx9MeQ/200.webp?cid=790b7611xpxt2gm2zlr6nh1gms4zhbxtc888eqy58j7xnjqe&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media3.giphy.com/media/Cx0JktG3wBWvu/200.webp?cid=ecf05e47mljo9efq0siojoh6qhrcviznvtezx2y5fgrjp41n&ep=v1_gifs_search&rid=200.webp&ct=g"
        ]
        return random.choice(large_image_list)
    
    if Size == "Extra Large":
        extralarge_image_list = [
        "https://giphy.com/gifs/fallontonight-jimmy-fallon-mono-tonightshow-yTSPaYi0GEJvR2DKLd",
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2NiOXpkcm9sdTY0Zm9oa3c4enQyaDdxdGh4eGd4dHlreThzaWhzdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fSYmbgG5Ug8S11K0FU/giphy.webp",
        "https://media2.giphy.com/media/l4FGoFe3zqcZtOblu/200.webp?cid=ecf05e47ge7d1n4o8g799qy7duiifpq6uiv87szcn2fhlm74&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media2.giphy.com/media/DmcvRyRdyVQrQ7NfjA/giphy.webp?cid=ecf05e47yl3t5ucl7rgyl2ze7xvxny2qom6tqo903vlfq6xp&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media1.giphy.com/media/e5uyWolyR0y30Wo1ya/200.webp?cid=790b7611xbkrgn8l9rycp2t6htoek0zxcqiu6ar9dlfbl5dh&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTZ4NnFsYzVjYW9iYTMzM3hscXh4aG9rNHZrYmN1eDJzb2xxbHN2byZlcD12MV9naWZzX3NlYXJjaCZjdD1n/sG4PBWRjI4GSVCDXEq/giphy.webp",
        "https://media1.giphy.com/media/rmJfgoakgxyDcc1BBP/giphy.webp?cid=ecf05e47xx9nf2d95kumz9eruj4rhlqyrq43g04fnu8lnfrm&ep=v1_gifs_search&rid=giphy.webp&ct=g"
        ]
        return random.choice(extralarge_image_list)
    
    if re.search(r'\bor\b', Size):
        or_list = [
        "https://media3.giphy.com/media/e9naycep2pz7OHQ4n0/200.webp?cid=790b7611zfyhtc2qm8bk14ui6higv1xqxjhzykhe13g79koz&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExemZ5aHRjMnFtOGJrMTR1aTZoaWd2MXhxeGpoenlraGUxM2c3OWtveiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0IF7LxXgYt4X9Bu/200.webp",
        "https://media2.giphy.com/media/5t9wJjyHAOxvnxcPNk/200.webp?cid=790b7611zfyhtc2qm8bk14ui6higv1xqxjhzykhe13g79koz&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media1.giphy.com/media/26DNgMmafrLA6x97i/giphy.webp?cid=790b7611zfyhtc2qm8bk14ui6higv1xqxjhzykhe13g79koz&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media0.giphy.com/media/fnmo7jLamKpqno5wuK/giphy.webp?cid=790b7611zfyhtc2qm8bk14ui6higv1xqxjhzykhe13g79koz&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media1.giphy.com/media/l3ODgW1tAz5acAIN93/giphy.webp?cid=790b7611zfyhtc2qm8bk14ui6higv1xqxjhzykhe13g79koz&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media3.giphy.com/media/geEvRnbQqLYsb5WOr8/giphy.webp?cid=ecf05e47pquq5bwey4yke4oagcrtqv7nd0lnauvsyaa0chp7&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media4.giphy.com/media/FCfd6Eb2pcpWlIHVq3/giphy.webp?cid=ecf05e47pquq5bwey4yke4oagcrtqv7nd0lnauvsyaa0chp7&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media4.giphy.com/media/eMJMuOnsrxam3TxFXd/200.webp?cid=ecf05e47l0et9elqdd7vkjrd2za6zmraly8vd3llxv92mmu5&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media4.giphy.com/media/BMtGb8JSk2Ln1cnPMA/200.webp?cid=ecf05e47l0et9elqdd7vkjrd2za6zmraly8vd3llxv92mmu5&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media3.giphy.com/media/Wmd9x19V1BZmTH0VHz/giphy.webp?cid=ecf05e47l0et9elqdd7vkjrd2za6zmraly8vd3llxv92mmu5&ep=v1_gifs_search&rid=giphy.webp&ct=g"
        ]
        return random.choice(or_list)
    else:
        return None
    
def size_method_avg(average_points):
    rounded = round(average_points)
    if average_points == 0:
        return ""
    if average_points < 1:
         return "Small"
    if rounded == 1:
        return "Small"
    if rounded == 2:
        return "Medium"
    if rounded == 3:
        return "Large"
    if rounded == 4:
        return "Extra Large"

def size_method_range(average_points):
    if average_points == 0:
        return ""
    if average_points <= 1.6:
        return "Small"
    elif average_points <= 2.3:
            return "Medium"
    elif average_points <= 3.1:
            return "Large"
    else:
        return "Extra Large"
    
def get_user_input(question, input_type, answers, key):

    if input_type == "Selectbox":
        options = [answer["text"] for answer in answers]
        # Use a unique key for each selectbox
        selection = st.selectbox(question, options, index=None, key=f"selectbox-{key}")

        points = sum(answer["points"] for answer in answers if answer["text"] == selection)
        return points

    elif input_type == "Radio":
        options = [answer["text"] for answer in answers]
        # Use a unique key for each radio button group
        selection = st.radio(question, options, index=None, key=f"radio-{key}")

        points = sum(answer["points"] for answer in answers if answer["text"] == selection)
        return points

    elif input_type == "Multiselect":
        options = [answer["text"] for answer in answers]
        # Use a unique key for each multiselect
        selections = st.multiselect(question, options, default=[], key=f"multiselect-{key}")
        points = sum(answer["points"] for answer in answers if answer["text"] in selections)
        return points

    return None

def display_complexity_question(question, input_type, answers, x):
    
    if input_type == "Selectbox":
        options = [answer["text"] for answer in answers]
        selection = st.selectbox(question, options, index=None, disabled= x)
        return selection

    elif input_type == "Radio":
        options = [answer["text"] for answer in answers]
        selection = st.radio(question, options, index=None, disabled =  x)
        return selection

    elif input_type == "Multiselect":
        options = [answer["text"] for answer in answers]
        selections = st.multiselect(question, options, default=[], disabled =  x)
        return selections

    return None