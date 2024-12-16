import pandas as pd


road_name_to_file = {
    "도로없음": "static/data/data.csv",
    "강남대로": "static/data/gangnam.csv",
    "논현로": "static/data/nonhyeon.csv",
    "도곡로": "static/data/dogok.csv",
    "도산로": "static/data/dosan.csv",
    "봉은사로": "static/data/bongeunsa.csv",
    "삼성로": "static/data/samsung.csv",
    "선릉로": "static/data/seolleung.csv",
    "압구정로": "static/data/apgujeong.csv",
    "역삼로": "static/data/yeoksam.csv",
    "영동대로": "static/data/yeongdong.csv",
    "온주로": "static/data/eonju.csv",
    "테헤란로": "static/data/teheran.csv",
    "학동로": "static/data/hakdong.csv",
}


def get_traffic_data(interval, road_name):

    data = pd.read_csv(road_name_to_file.get(road_name))

    data.fillna(0, inplace=True)

    data["traffic_volume"] = data["entered"] + data["departed"]

    interval = int(interval)
    # 시간 구간 필터링
    filtered_data = data[data["interval"] == interval]

    # 시간별 그룹화하여 통행량 계산
    response = (
        filtered_data.groupby(["interval", "id"], as_index=False)
        .agg(
            {
                "traffic_volume": "sum",  # 통행량 합계
                "speed": "mean",  # 평균 속도
                "congestion_level": "max",  # 혼잡도 (최대값 또는 다른 통계 기준 사용 가능)
            }
        )
        .sort_values(by=["interval", "id"])
    )
    return response


def get_data_with_hours(road_name, road_ids):
    data = pd.read_csv(road_name_to_file.get(road_name))
    data.fillna(0, inplace=True)
    data["traffic_volume"] = data["entered"] + data["departed"]
    filtered_data = data[data["id"].isin(road_ids)]

    grouped_data = (
        filtered_data.groupby("interval", as_index=False)
        .agg({"traffic_volume": "sum", "speed": "mean"})
        .sort_values(by="interval")
    )
    return grouped_data
