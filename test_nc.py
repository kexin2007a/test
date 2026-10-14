import netCDF4
import pandas as pd

print("===读取NC文件===", flush=True)
nc = netCDF4.Dataset("era5_2021_02.nc")

# 查看变量信息
var_names = list(nc.variables.keys())
print("变量：", var_names[:6], flush=True)

# 读取三个核心维度
time = nc["time"][:]
lat = nc["latitude"][:]
lon = nc["longitude"][:]
tp = nc["tp"][:] # tp总降水，单位m

# 转为DataFrame，展平
import numpy as np
time_arr, lat_arr, lon_arr = np.meshgrid(time, lat, lon, indexing="ij")

df = pd.DataFrame({
    "time": time_arr.flatten(),
    "lat": lat_arr.flatten(),
    "lon": lon_arr.flatten(),
    "precip_m": tp.flatten()
})
# 降水单位米转毫米
df["precip_mm"] = df["precip_m"] * 1000

df.to_csv("era5_2022_01_foziling.csv", index=False)
print("✅ 导出CSV完成！", flush=True)
nc.close()