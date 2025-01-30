from folium import Map, Marker

map = Map(location=[37.517, 126.96], zoom_start=13, tiles="CartoDB Voyager")  # 지도 생성
marker = Marker(location=[37.517, 126.96], tooltip="노들섬 맹꽁이 숲")  # 마커 생성
marker.add_to(map)  # 마커를 지도에 추가
map
