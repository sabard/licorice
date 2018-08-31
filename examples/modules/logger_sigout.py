scalar_out[0] = scalar_outRaw[scalar_outBufVars[8]][0]
if scalar_out[0] < 255:
    scalar_out[0] += 1
else:
    scalar_out[0] = 0

vector_ints[:] = vector_intsRaw[vector_intsBufVars[8]][:]
if vector_ints[0] < 0 :
    vector_ints[:] += 5
else:
    vector_ints[0] = -32767 
    vector_ints[1] = -20000
    vector_ints[2] = -10000

vector_floats[:] = vector_floatsRaw[vector_floatsBufVars[8]][:]
if vector_floats[0] < 1e9 :
    vector_floats[:] *= 2
else:
    vector_floats[:] = [1, 2, 3, 4]

matrix_out[:] = matrix_outRaw[matrix_outBufVars[8]][:]
if matrix_out[0, 0] < 1e10 :
    matrix_out *= 3
else:
    matrix_out[:, :] = [ [1, 2], [3, 4] ]