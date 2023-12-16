import numpy as np
from scipy.interpolate import CubicSpline
import os

def _transpose(matrix):
    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]  
    return result

def _SRS(path):
    all_file_name = os.listdir(path)
    SRS_file = []
    
    for j in range(len(all_file_name)):
        if ".txt" in str(all_file_name[j]) and "SRS" in str(all_file_name[j]):
            SRS_file.append(all_file_name[j]) 
    return SRS_file

def _handle_SRS_data(SRS_file_name):
    read_file_path = "./calibration_data/" + SRS_file_name
    SRS_data = np.loadtxt(read_file_path, dtype = "str", delimiter = "\t")
    TSRS = _transpose(SRS_data)
    SRS_wavelength = []
    SRS_absorbance = []
    for i in range(2, len(TSRS[0])):
        wav_data = int(TSRS[0][i])
        abs_data = float(TSRS[1][i])
        SRS_wavelength.append(wav_data)
        SRS_absorbance.append(abs_data)
    return SRS_wavelength, SRS_absorbance

def _ref(path):
    all_file_name = os.listdir(path)
    ref_file = []
    
    for j in range(len(all_file_name)):
        if ".csv" in str(all_file_name[j]) and "ref" in str(all_file_name[j]):
            ref_file.append(all_file_name[j]) 
    return ref_file

def _raw(path):
    all_file_name = os.listdir(path)
    raw_file = []
    
    for j in range(len(all_file_name)):
        if ".csv" in str(all_file_name[j]):
            raw_file.append(all_file_name[j]) 
    return raw_file

def _Raw_CubicSpline(wavelength, intensity):
    cubic_calculate = CubicSpline(wavelength, intensity)
    
    raw_wavelength = []
    raw_intensity = []
    for j in range(950, 1700):
        intensity_at_target_wavelength = float(cubic_calculate(j))
        raw_wavelength.append(j)
        raw_intensity.append(intensity_at_target_wavelength)
    return (raw_wavelength, raw_intensity)
    
def _CubicSpline(file_name):
    read_file_path = "./calibration_data/" + file_name
    data_list = np.loadtxt(read_file_path, dtype = "float", delimiter = ",", skiprows=1)
    data_list = _transpose(data_list)
    
    cubic_test = CubicSpline(data_list[0], data_list[1])
    
    integer_wavelength = []
    integer_intensity = []
    for j in range(950, 1700):
        intensity_at_target_wavelength = float(cubic_test(j))
        integer_wavelength.append(j)
        integer_intensity.append(intensity_at_target_wavelength)
    return (file_name, integer_wavelength, integer_intensity)

def _ref_CubicSpline_inter_data(ref_file):
    _cubic_intensity = []
    _cubic_wave = []
    for i in range(len(ref_file)):
        file_name, integer_wavelength, cubic_intensity = _CubicSpline(ref_file[i])
        _cubic_intensity.append(cubic_intensity)
        _cubic_wave = integer_wavelength
    return _cubic_intensity, _cubic_wave

def _SRS_Array_integration(SRS_file):
    _SRS = []
    _SRS_wavelength = []
    
    for j in range(len(SRS_file)):
        SRS_wavelength, SRS_absorbance = _handle_SRS_data(SRS_file[j])
        _SRS.append(SRS_absorbance)
        _SRS_wavelength = SRS_wavelength
    return _SRS, _SRS_wavelength

def _corresponding_wavelength_all_data(_SRS_wavelength, cubicspline_abs_4_intensity,_cubic_wave):
    corresponding_absorbance = []
    for a in range(len(_SRS_wavelength)):
        if _SRS_wavelength[a] in _cubic_wave:
            corresponding_absorbance.append(cubicspline_abs_4_intensity[a])
    return corresponding_absorbance
    
def _result_CubicSpline_reflection_data(cubicspline_ref_4_intensity, corresponding_absorbance, predict_intensity, _cubic_wave):
    _reflection = []
    for r in range(len(_cubic_wave)):
        cubic_reflection_return = CubicSpline(cubicspline_ref_4_intensity[r], corresponding_absorbance[r])
        #print("at" + str(_cubic_wave[r]) + "of spline formula building successfully")
        reflection_data = float(cubic_reflection_return(predict_intensity[r]))
        _reflection.append(reflection_data)
        #print("at" + str(_cubic_wave[r]) + "of spline formula building successfully")
    return _reflection
##testing
def _result_CubicSpline_reflection_data__2(cubicspline_ref_4_intensity, corresponding_absorbance, _cubic_wave):
    for r in range(len(_cubic_wave)):
        cubic_reflection_return = CubicSpline(cubicspline_ref_4_intensity[r], corresponding_absorbance[r])
        #print("at" + str(_cubic_wave[r]) + "of spline formula building successfully")

def _raw_file_encoding(read_file_path):
    raw_data = np.loadtxt(read_file_path, dtype = "str", delimiter = ",")
    
    raw_wavelength = []
    raw_sample = []
    raw_reference = []
    for i in range(len(raw_data)):
        raw_element_sample = []
        if raw_data[i][0] == 'Wavelength (nm)':
            for j in range(1, len(raw_data[i])):
                add_data = float(raw_data[i][j])
                raw_wavelength.append(add_data)
        elif raw_data[i][0] == 'Reference Signal (unitless)':
            for r in range(1, len(raw_data[i])):
                add_data = float(raw_data[i][r])
                raw_reference.append(add_data)
        elif raw_data[i][0] == 'Sample Signal (unitless)':
            for k in range(1, len(raw_data[i])):
                add_data = float(raw_data[i][k])
                raw_element_sample.append(add_data)
            raw_sample.append(raw_element_sample)
    return raw_wavelength, raw_sample, raw_reference



















