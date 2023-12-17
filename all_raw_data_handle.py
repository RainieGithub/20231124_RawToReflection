import numpy as np
from scipy.interpolate import CubicSpline
import os
import predict_reflection_cubicspline_py2 as prc
import csv

path = "C:/Users/user/Desktop/_RawToReflection/"


path_raw = path + "raw_data/"
path_cal = path + "calibration_data/"
path_cal = path_cal.replace('/', '//')
path_save = path + "reflection_data/"
raw_file = prc._raw(path_raw) #印出csv檔案

for j in range(len(raw_file)):
    print("NO. " + str(j) + str(raw_file[j]))
    read_file_path = path_raw + raw_file[j]
    str_name = raw_file[j].replace(".csv", "")
    raw_wavelength, raw_sample, raw_reference = prc._raw_file_encoding(read_file_path)
    
    ref_file = prc._ref(path_cal)
    _cubic_intensity, _cubic_wave= prc._ref_CubicSpline_inter_data(ref_file)
    
    SRS_file = prc._SRS(path_cal)
    _SRS, _SRS_wavelength = prc._SRS_Array_integration(SRS_file)
    
    cubicspline_ref_4_intensity = prc._transpose(_cubic_intensity)
    cubicspline_abs_4_intensity = prc._transpose(_SRS)
    corresponding_absorbance = prc._corresponding_wavelength_all_data(_SRS_wavelength, cubicspline_abs_4_intensity, _cubic_wave)
    
    save_data = []
    #處理標準白吸收度
    _result_wavelength, _result_reference = prc._Raw_CubicSpline(raw_wavelength, raw_reference)
    _reference_reflection = prc._result_CubicSpline_reflection_data(cubicspline_ref_4_intensity, corresponding_absorbance, _result_reference, _cubic_wave)
    _reference_reflection.insert(0, np.array('Reference'))
    _result_wavelength.insert(0, np.array('Wavelength'))
    
    save_data.append(_result_wavelength)
    save_data.append(_reference_reflection)
    #處理樣品吸收度
    _sample_reflection = []
    for i in range(len(raw_sample)):
        _result_wavelength, raw_sample_data = prc._Raw_CubicSpline(raw_wavelength, raw_sample[i])
        _sample_reflection_data = prc._result_CubicSpline_reflection_data(cubicspline_ref_4_intensity, corresponding_absorbance, raw_sample_data, _cubic_wave)
        _sample_reflection_data.insert(0, np.array(str_name))
        _sample_reflection.append(_sample_reflection_data)
        save_data.append(_sample_reflection_data)
    #print(save_data)
    
    a = np.array(save_data)
    np.savetxt(path_save + raw_file[j], a, fmt='%s', delimiter = ",")
