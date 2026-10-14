import xarray as xr
import pandas as pd
ds=xr.open_dataset("era5_2021_02.nc",
engine="netcdf4")
df=ds.to_dataframe()
df.to_excel("era5_output1.xlsx")
print("nc文件读取成功，已导出")