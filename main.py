import polynomial

gr_x = 2
coef_x = '1/3;1/2;1/4'
gr_y = 1
coef_y = '1/3;1/2'

x = polynomial.STR_TO_POL(gr_x, coef_x)
y = polynomial.STR_TO_POL(gr_y, coef_y)
res = polynomial.MUL_PP_P(x,y)
print(res)