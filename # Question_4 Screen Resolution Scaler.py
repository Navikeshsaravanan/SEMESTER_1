# Question_4 Screen Resolution Scaler
def scale_resolutions(resolutions,factor):
    final_resolutions = []
    for i in resolutions:
        a,b = i
        a *= factor
        b *= factor
        h = (a,b)
        final_resolutions.append(h)
    print(final_resolutions)
resolutis = eval(input("enter the resolutions in the form of lists:"))
facto = float(input("enter the factor:"))
scale_resolutions(resolutis,facto)