# predict_reflection_cublicspline_py2 Function Documentation:

## _transpose(matrix):

  function : Return transpose the array.
  
  "matrix" parameter: Array variable requiring transposition.


## _SRS(path):

  function : Return an array of file names containing both 'SRS' and '.txt' in the searched folder.
  
  "path" parameter: Retrieve the folder path.
  

## _handle_SRS_data(SRS_file_name):

  function : Return wavelength and absorbance values from SRS file names.
  
  "SRS_file_name": File names containing the term 'SRS'.
  

## _ref(path):

  function : Return an array of file names containing both 'ref' and '.csv' in the searched folder.
  
  "path" parameter: Retrieve the folder path.
  
  
## _raw(path):

  function : Return an array of file names containing the '.csv' pattern in the searched folder.
  
  "path" parameter: Retrieve the folder path.
  

## _Raw_CubicSpline(wavelength, intensity):

  function : Return two arrays, one representing the wavelength and the other representing the intensity, both individually interpolated using CubicSpline.
  
  "wavelength" parameter: raw wavelength
  
  "intensity" parameter: raw intensity
  

## _CubicSpline(file_name): 

  function : After reading the arrays of wavelength and intensity from the file names, return new arrays of wavelength and intensity, processed through CubicSpline interpolation.
  
  "file_name" parameter : The file names to be read.
  

## _ref_CubicSpline_inter_data(ref_file):

  function : After reading the file names returned by _ref(path), merge the intensities from the read file names, and return a two-dimensional array.
  
  "ref_file" parameter : returned by _ref(path)
  

## _SRS_Array_integration(SRS_file):

  function : After reading the file names returned by _SRS(path), merge the absorbance values from the read file names, and return a two-dimensional array.
  
  "SRS_file" parameter : returned by _SRS(path)
  

## _corresponding_wavelength_all_data(_SRS_wavelength, cubicspline_abs_4_intensity,_cubic_wave):

  function : Map the corresponding SRS wavelength ranges to cubic_wave, and search for the corresponding positions in cubicspline_abs_4_intensity, which represents the absorbance values of SRS.
  
  "_SRS_wavelength" parameter : SRS wavelength range.
  
  "cubicspline_abs_4_intensity" parameter : The standard white absorbance corresponding to the SRS wavelength ranges for four different intensity segments.[02, 50, 75, 99]
  
  "_cubic_wave" parameter : The mapping of _ref_CubicSpline_inter_data(ref_file) to the standard white cubic_wave.
  

## _result_CubicSpline_reflection_data(cubicspline_ref_4_intensity, corresponding_absorbance, predict_intensity, _cubic_wave):

  function : By incorporating cubicspline_ref_4_intensity, corresponding_absorbance, predict_intensity, and _cubic_wave, the resulting array _reflection represents the transformation of the original data into reflectance values.
  
  "cubicspline_ref_4_intensity" parameter : The standard white absorbance corresponding to the SRS wavelength ranges for four different intensity segments.[02, 50, 75, 99]
  
  "corresponding_absorbance" parameter : The return value of _corresponding_wavelength_all_data(_SRS_wavelength, cubicspline_abs_4_intensity, _cubic_wave) is corresponding_absorbance.
  
  "predict_intensity" parameter : Predicting intensity involves transforming the array that needs to be predicted, which is the original data to be converted into reflectance values.

  "_cubic_wave" parameter :  The mapping of _ref_CubicSpline_inter_data(ref_file) to the standard white cubic_wave.
  
## _raw_file_encoding(read_file_path):

  function: Read the file names of raw data from the specified folder and return three arrays from the raw data, namely raw_wavelength, raw_sample, and raw_reference.

  read_file_path:The file names to be read.

  
