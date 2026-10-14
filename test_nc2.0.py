
import xarray as xr
import pandas as pandas

ds=xr.open_dataset("era5_2021_02/data_0.nc",engine="netcdf4")
#print(ds)
df=ds.to_dataframe().reset_index()
df["tp_mm"]=df["tp"]*1000
df.to_csv("era5_2021_02.csv",index=False,encoding="utf-8")
print("csv导出成功！")

#import magic
#print(magic.from_file("era5_2022_02.nc"))
