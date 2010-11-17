# Copyright 2010 The Fatiando a Terra Development Team
#
# This file is part of Fatiando a Terra.
#
# Fatiando a Terra is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Fatiando a Terra is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Fatiando a Terra.  If not, see <http://www.gnu.org/licenses/>.
"""
Unit tests for :mod:`fatiando.seismo.traveltime`
"""
__author__ = 'Leonardo Uieda (leouieda@gmail.com)'
__date__ = 'Created 28-Mar-2010'

import unittest

import fatiando.seismo.traveltime


class CartesianStraightTestCase(unittest.TestCase):
    """Test case for :func:`fatiando.seismo.traveltime.cartesian_straight`"""
    
    label = 'fast'

    def setUp(self):

        # Arguments: [S   x1  y1  x2  y2  xf   yf   xr  yr], t
        vertical = [ \
            ([1., 1., 1., 2., 2., 1.5, 0., 1.5, 3.], 1.), \
            ([2., 1., 1., 3., 2., 1.5, 0., 1.5, 3.], 2.), \
            ([0.5, 1., 1., 2., 3., 1.5, 0., 1.5, 3.], 1.), \
            ([1., 1., 1., 2., 2., 1.5, 0., 1.5, 1.3], 0.3), \
            ([2., 1., 1., 3., 2., 1.5, 1.7, 1.5, 2.], 0.6), \
            ([0.5, 1., 1., 2., 3., 1.5, 1., 1.5, 2.8], 0.9) ]
        vertical_border = [\
            ([1., 1., 1., 2., 2., 1., 0., 1., 3.], 1.), \
            ([2., 1., 1., 3., 2., 3., 0., 3., 3.], 2.), \
            ([0.5, 1., 1., 2., 3., 2., 0., 2., 3.], 1.), \
            ([1., 1., 1., 2., 2., 2., 0., 2., 1.3], 0.3), \
            ([2., 1., 1., 3., 2., 1., 1.7, 1., 2.], 0.6), \
            ([0.5, 1., 1., 2., 3., 1., 1., 1., 2.8], 0.9) ]
        horizontal = [ \
            ([1., 1., 1., 2., 2., 0., 1.5, 3., 1.5], 1.), \
            ([2., 1., 1., 2., 3., 0., 1.5, 5., 1.5], 2.), \
            ([3., 1., 1., 3., 2., 0., 1.5, 10., 1.5], 6.), \
            ([1., 1., 1., 2., 2., 1.5, 1.5, 3., 1.5], 0.5), \
            ([2., 1., 1., 2., 3., 1.2, 1.5, 5., 1.5], 1.6), \
            ([3., 1., 1., 3., 2., 0., 1.5, 1.4, 1.5], 1.2) ]
        horizontal_border = [\
            ([1., 1., 1., 2., 2., 0., 1., 3., 1.], 1.), \
            ([2., 1., 1., 2., 3., 0., 3., 5., 3.], 2.), \
            ([3., 1., 1., 3., 2., 0., 2., 10., 2.], 6.), \
            ([1., 1., 1., 2., 2., 1.5, 2., 3., 2.], 0.5), \
            ([2., 1., 1., 2., 3., 1.2, 1., 5., 1.], 1.6), \
            ([3., 1., 1., 3., 2., 0., 1., 1.4, 1.], 1.2) ]
        not_passing = [\
            ([1., 0., 0., 2., 2., 3., 0., 4., 1.5], 0.), \
            ([2., -1., 2., 1., 3., 0., 0., -10., -2.], 0.) , \
            ([1.5, 2., 0., 3., 10., 0., 0., 0., 10.], 0.) ]
        src_rec_inside = [\
            ([1., 0., 0., 2., 2., 1, 1, 1, 1.5], 0.5) ]
        general_cases = [\
            ([1., 2., 0., 3., 1., 0., 2.4, 3.0, 0.4], 1.081665383)]


        self.known = []
        self.known.extend(vertical)
        self.known.extend(vertical_border)
        self.known.extend(horizontal)
        self.known.extend(horizontal_border)
        self.known.extend(not_passing)
        self.known.extend(src_rec_inside)
        self.known.extend(general_cases)


    def test_known_values(self):
        "seismo.traveltime.cartesian_straight returns correct values"

        tnum = 0
        for args, t_known in self.known:

            tnum += 1

            t_my = fatiando.seismo.traveltime.cartesian_straight(*args)

            self.assertAlmostEquals(t_my, t_known, places=8, \
                msg='Failed test case %d. t_my=%.10g  t_known=%.10g' \
                % (tnum, t_my, t_known))

        
# Return the test suit for this module
################################################################################
def suite(label='fast'):

    testsuite = unittest.TestSuite()

    CartesianStraightTestCase.label = label
    testsuite.addTest(unittest.makeSuite(CartesianStraightTestCase, \
                                         prefix='test'))
    
    return testsuite

################################################################################


if __name__ == '__main__':

    unittest.main(defaultTest='suite')