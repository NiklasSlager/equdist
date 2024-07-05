import jax.numpy as jnp

def psat_params():
    return jnp.array([[ 2.76921e+01, -1.32440e+03,  0.00000e+00,  0.00000e+00,
        -3.43660e+00,  3.10190e-05,  2.00000e+00,  9.06900e+01,
         1.90560e+02],
       [ 4.03441e+01, -2.59870e+03,  0.00000e+00,  0.00000e+00,
        -5.12830e+00,  1.49130e-05,  2.00000e+00,  9.03500e+01,
         3.05320e+02],
       [ 4.75651e+01, -3.49260e+03,  0.00000e+00,  0.00000e+00,
        -6.06690e+00,  1.09190e-05,  2.00000e+00,  8.54700e+01,
         3.69830e+02],
       [ 5.48301e+01, -4.36320e+03,  0.00000e+00,  0.00000e+00,
        -7.04600e+00,  9.45090e-06,  2.00000e+00,  1.34860e+02,
         4.25120e+02],
       [ 6.72281e+01, -5.42030e+03,  0.00000e+00,  0.00000e+00,
        -8.82530e+00,  9.61710e-06,  2.00000e+00,  1.43420e+02,
         4.69700e+02],
       [ 5.97951e+01, -4.97600e+03,  0.00000e+00,  0.00000e+00,
        -7.71690e+00,  8.72710e-06,  2.00000e+00,  1.13250e+02,
         4.60400e+02],
       [ 7.63161e+01, -6.99640e+03,  0.00000e+00,  0.00000e+00,
        -9.88020e+00,  7.20990e-06,  2.00000e+00,  1.82570e+02,
         5.40200e+02],
       [ 8.45711e+01, -7.90020e+03,  0.00000e+00,  0.00000e+00,
        -1.10030e+01,  7.18020e-06,  2.00000e+00,  2.16380e+02,
         5.68700e+02]], dtype=float)

def cpvap_params():
    return jnp.array([[   7.95309,   19.0917 , 2086.9    ,    9.93647,  991.96   ,
          50.     , 1500.     ],
       [  10.5704 ,   20.2391 ,  872.24   ,   16.0337 , 2430.4    ,
         298.15   , 1500.     ],
       [  14.2051 ,   30.2403 ,  844.31   ,   20.5802 , 2482.7    ,
         298.15   , 1500.     ],
       [  19.1445 ,   38.7934 ,  841.49   ,   25.258  , 2476.1    ,
         298.15   , 1500.     ],
       [  21.0304 ,   71.9165 , 1650.2    ,   45.1896 ,  747.6    ,
         200.     , 1500.     ],
       [  17.8179 ,   77.9832 , 1545.     ,   45.9301 ,  666.7    ,
         200.     , 1500.     ],
       [  28.6973 ,   95.5622 , 1676.6    ,   65.4438 ,  756.4    ,
         200.     , 1500.     ],
       [  32.3732 ,  105.833  , 1635.6    ,   72.9435 ,  746.4    ,
         200.     , 1500.     ]], dtype=float)

def hvap_params():
    return jnp.array([[ 2.43480e+00,  2.60870e-01, -1.46940e-01,  2.21540e-01,
         0.00000e+00, -1.82460e+02, -8.25900e+01],
       [ 5.03750e+00,  6.06460e-01, -5.54920e-01,  3.27990e-01,
         0.00000e+00, -1.82800e+02,  3.21700e+01],
       [ 6.97645e+00,  7.82370e-01, -7.73190e-01,  3.92460e-01,
         0.00000e+00, -1.87680e+02,  9.66800e+01],
       [ 8.65530e+00,  8.33700e-01, -8.22740e-01,  3.96130e-01,
         0.00000e+00, -1.38290e+02,  1.51970e+02],
       [ 1.07688e+01,  9.58860e-01, -9.23840e-01,  3.93930e-01,
         0.00000e+00, -1.29730e+02,  1.96550e+02],
       [ 1.01103e+01,  9.54480e-01, -9.82890e-01,  4.57190e-01,
         0.00000e+00, -1.59900e+02,  1.87250e+02],
       [ 1.25432e+01,  5.12830e-01, -1.09820e-01, -1.01800e-02,
         0.00000e+00, -9.05800e+01,  2.67050e+02],
       [ 1.60356e+01,  1.07690e+00, -1.01240e+00,  3.70750e-01,
         0.00000e+00, -5.67700e+01,  2.95550e+02]], dtype=float)

def hform_params():
    return jnp.array([ -74.47018 ,  -83.7641  , -104.61004 , -125.705765, -146.66176 , -153.59715 , -187.52437 , -208.61047 ], dtype=float)
