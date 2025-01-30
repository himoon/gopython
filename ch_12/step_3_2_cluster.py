from folium import Map, Marker
from folium.plugins import MarkerCluster

map = Map(location=[37.517, 126.96], zoom_start=14, tiles="CartoDB Voyager")  # 지도 생성
cluster = MarkerCluster().add_to(map)  # 마커 클러스터 생성 및 지도에 추가
for num in range(5):
    marker = Marker(location=[37.517, 126.96 + num / 1000])  # 마커 생성
    marker.add_to(cluster)  # 마커를 마커 클러스트에 추가
map
