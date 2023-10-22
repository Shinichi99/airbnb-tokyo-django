from django.shortcuts import render
from django.http import HttpResponse
import numpy as np


# Create your views here.
def index(request):
    return render(request, 'index.html')

def getPredictions(variables):
    import pickle
    model = pickle.load(open("airbnb_tokyo_app/model.sav", "rb"))
    prediction = int(model.predict(variables))
    return prediction

def result(request):
    import pandas as pd
    from geopy.distance import geodesic

    Shinjuku_ku = 0
    Minato_ku = 0
    Katsushika_ku = 0
    Taito_ku = 0
    Itabashi_ku = 0
    Toshima_ku = 0
    Sumida_ku = 0
    Shinagawa_ku = 0
    Kita_ku = 0
    Adachi_ku = 0
    Nakano_ku = 0
    Shibuya_ku = 0
    Arakawa_ku = 0
    Chuo_ku = 0
    Suginami_ku = 0
    Nerima_ku = 0
    Setagaya_ku = 0
    Bunkyo_ku = 0
    Edogawa_ku = 0
    Ota_ku = 0
    Koto_ku = 0
    Chiyoda_ku = 0
    Meguro_ku = 0



    Entire_home_apt = 0
    Private_room = 0
    Hotel_room = 0
    Shared_room = 0

    Hair_dryer = 0
    Smoke_alarm = 0
    Essentials = 0
    Wifi = 0
    Shampoo = 0
    Hangers = 0
    Fire_extinguisher = 0
    Kitchen = 0
    Hot_water = 0
    Air_conditioning = 0
    Refrigerator = 0
    Microwave = 0
    Heating = 0
    Dishes_and_silverware = 0
    Self_check_in = 0
    Long_term_stays_allowed = 0
    Washer = 0
    Bed_linens = 0
    TV = 0
    Iron = 0
    Carbon_monoxide_alarm = 0
    Hot_water_kettle = 0
    Conditioner = 0
    Bathtub = 0
    Body_soap = 0
    Private_entrance = 0
    Cooking_basics = 0
    Cleaning_products = 0
    Room_darkening_shades = 0
    Dedicated_workspace = 0
    Stove = 0
    Lockbox = 0
    Bidet = 0
    Elevator = 0
    Security_cameras_on_property = 0
    Freezer = 0
    Rice_maker = 0
    Luggage_dropoff_allowed = 0
    First_aid_kit = 0
    Dining_table = 0
    Shower_gel = 0
    Extra_pillows_and_blankets = 0
    Laundromat_nearby = 0
    Dryer = 0
    Paid_parking_off_premises = 0
    Free_washer = 0
    Ethernet_connection = 0
    Keypad = 0
    Patio_or_balcony = 0
    Drying_rack_for_clothing = 0


    latitude = float(request.GET['latitude'])
    longitude = float(request.GET['longitude'])
    ku = request.GET['ku']
    if ku == 'Shinjuku Ku':
        Shinjuku_ku = 1
    elif ku == 'Minato Ku':
        Minato_ku = 1
    elif ku == 'Katsushika Ku':
        Katsushika_ku = 1
    elif ku == 'Taito Ku':
        Taito_ku = 1
    elif ku == 'Itabashi Ku':
        Itabashi_ku = 1
    elif ku == 'Toshima Ku':
        Toshima_ku = 1
    elif ku == 'Sumida Ku':
        Sumida_ku = 1
    elif ku == 'Shinagawa Ku':
        Shinagawa_ku = 1
    elif ku == 'Kita Ku':
        Kita_ku = 1
    elif ku == 'Adachi Ku':
        Adachi_ku = 1
    elif ku == 'Nakano Ku':
        Nakano_ku = 1
    elif ku == 'Shibuya Ku':
        Shibuya_ku = 1
    elif ku == 'Arakawa Ku':
        Arakawa_ku = 1
    elif ku == 'Chuo Ku':
        Chuo_ku = 1
    elif ku == 'Suginami Ku':
        Suginami_ku = 1
    elif ku == 'Nerima Ku':
        Nerima_ku = 1
    elif ku == 'Setagaya Ku':
        Setagaya_ku = 1
    elif ku == 'Bunkyo Ku':
        Bunkyo_ku = 1
    elif ku == 'Edogawa Ku':
        Edogawa_ku = 1
    elif ku == 'Ota Ku':
        Ota_ku = 1
    elif ku == 'Koto Ku':
        Koto_ku = 1
    elif ku == 'Chiyoda Ku':
        Chiyoda_ku = 1
    elif ku == 'Meguro Ku':
        Meguro_ku = 1
    
    df_station = pd.read_csv('airbnb_tokyo_app/station20230907free.csv')
    df_station_tokyo = df_station[df_station['pref_cd'] == 13]
    def get_distance(lat, lon, df_station):
        distances = []
        for idx, row in df_station.iterrows():
            distances.append(geodesic((lat, lon), (row['lat'], row['lon'])).km)
        return min(distances)
    distance_to_station = get_distance(latitude, longitude, df_station_tokyo)

    


    tokyo_station = [35.681236, 139.767125]
    shinjuku_station = [35.690921, 139.700257]

    distance_to_tokyo_station = geodesic((latitude, longitude), tokyo_station).km
    distance_to_shinjuku_station = geodesic((latitude, longitude), shinjuku_station).km

    room_type = request.GET['room_type']
    if room_type == 'Entire home/apt':
        Entire_home_apt = 1
    elif room_type == 'Private room':
        Private_room = 1
    elif room_type == 'Hotel room':
        Hotel_room = 1
    else:
        Shared_room = 1
    accommodates = int(request.GET['accommodates'])
    bedrooms = int(request.GET['bedrooms'])
    beds = int(request.GET['beds'])
    bathrooms = int(request.GET['bathrooms'])
    bathrooms_shared = int(request.GET['bathrooms_shared'])
    minimum_nights = int(request.GET['minimum_nights'])

    Hair_dryer = int(request.GET.get('Hair dryer', 0))
    Smoke_alarm = int(request.GET.get('Smoke alarm', 0))
    Essentials = int(request.GET.get('Essentials', 0))
    Wifi = int(request.GET.get('Wifi', 0))
    Shampoo = int(request.GET.get('Shampoo', 0))
    Hangers = int(request.GET.get('Hangers', 0))
    Fire_extinguisher = int(request.GET.get('Fire extinguisher', 0))
    Kitchen = int(request.GET.get('Kitchen', 0))
    Hot_water = int(request.GET.get('Hot water', 0))
    Air_conditioning = int(request.GET.get('Air conditioning', 0))
    Refrigerator = int(request.GET.get('Refrigerator', 0))
    Microwave = int(request.GET.get('Microwave', 0))
    Heating = int(request.GET.get('Heating', 0))
    Dishes_and_silverware = int(request.GET.get('Dishes and silverware', 0))
    Self_check_in = int(request.GET.get('Self check-in', 0))
    Long_term_stays_allowed = int(request.GET.get('Long term stays allowed', 0))
    Washer = int(request.GET.get('Washer', 0))
    Bed_linens = int(request.GET.get('Bed linens', 0))
    TV = int(request.GET.get('TV', 0))
    Iron = int(request.GET.get('Iron', 0))
    Carbon_monoxide_alarm = int(request.GET.get('Carbon monoxide alarm', 0))
    Hot_water_kettle = int(request.GET.get('Hot water kettle', 0))
    Conditioner = int(request.GET.get('Conditioner', 0))
    Bathtub = int(request.GET.get('Bathtub', 0))
    Body_soap = int(request.GET.get('Body soap', 0))
    Private_entrance = int(request.GET.get('Private entrance', 0))
    Cooking_basics = int(request.GET.get('Cooking basics', 0))
    Cleaning_products = int(request.GET.get('Cleaning products', 0))
    Room_darkening_shades = int(request.GET.get('Room-darkening shades', 0))
    Dedicated_workspace = int(request.GET.get('Dedicated workspace', 0))
    Stove = int(request.GET.get('Stove', 0))
    Lockbox = int(request.GET.get('Lockbox', 0))
    Bidet = int(request.GET.get('Bidet', 0))
    Elevator = int(request.GET.get('Elevator', 0))
    Security_cameras_on_property = int(request.GET.get('Security cameras on property', 0))
    Freezer = int(request.GET.get('Freezer', 0))
    Rice_maker = int(request.GET.get('Rice maker', 0))
    Luggage_dropoff_allowed = int(request.GET.get('Luggage dropoff allowed', 0))
    First_aid_kit = int(request.GET.get('First aid kit', 0))
    Dining_table = int(request.GET.get('Dining table', 0))
    Shower_gel = int(request.GET.get('Shower gel', 0))
    Extra_pillows_and_blankets = int(request.GET.get('Extra pillows and blankets', 0))
    Laundromat_nearby = int(request.GET.get('Laundromat nearby', 0))
    Dryer = int(request.GET.get('Dryer', 0))
    Paid_parking_off_premises = int(request.GET.get('Paid parking off premises', 0))
    Free_washer = int(request.GET.get('Free washer', 0))
    Ethernet_connection = int(request.GET.get('Ethernet connection', 0))
    Keypad = int(request.GET.get('Keypad', 0))
    Patio_or_balcony = int(request.GET.get('Patio or balcony', 0))
    Drying_rack_for_clothing = int(request.GET.get('Drying rack for clothing', 0))






    input = np.array([[ latitude   , longitude   ,   accommodates        ,   bedrooms        ,
          beds       ,   minimum_nights        ,  Shinjuku_ku, Minato_ku, Katsushika_ku, Taito_ku, Itabashi_ku,
            Toshima_ku, Sumida_ku, Shinagawa_ku, Kita_ku, Adachi_ku, Nakano_ku, Shibuya_ku, Arakawa_ku,
              Chuo_ku, Suginami_ku, Nerima_ku, Setagaya_ku, Bunkyo_ku, Edogawa_ku, Ota_ku, Koto_ku, Chiyoda_ku, Meguro_ku
      ,   distance_to_station,   distance_to_tokyo_station,   distance_to_shinjuku_station,
          Entire_home_apt        ,   Private_room        ,   Hotel_room       ,   Shared_room       ,
          bathrooms        ,   bathrooms_shared,       Hair_dryer, Smoke_alarm, Essentials, Wifi,
            Shampoo, Hangers, Fire_extinguisher, Kitchen, Hot_water, Air_conditioning, Refrigerator,
              Microwave, Heating, Dishes_and_silverware, Self_check_in, Long_term_stays_allowed, Washer, Bed_linens,
            TV, Iron, Carbon_monoxide_alarm, Hot_water_kettle, Conditioner, Bathtub, Body_soap, Private_entrance,
              Cooking_basics, Cleaning_products, Room_darkening_shades, Dedicated_workspace, Stove, Lockbox, Bidet,
                Elevator, Security_cameras_on_property, Freezer, Rice_maker, Luggage_dropoff_allowed, First_aid_kit, Dining_table,
                  Shower_gel, Extra_pillows_and_blankets, Laundromat_nearby, Dryer, Paid_parking_off_premises, Free_washer, Ethernet_connection,
                    Keypad, Patio_or_balcony, Drying_rack_for_clothing
    ]])

    result = getPredictions(input)

    return render(request, 'result.html', {'result':result})