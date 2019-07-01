import numpy as np

from tslearn.piecewise import OneD_SymbolicAggregateApproximation, \
    SymbolicAggregateApproximation

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def test_sax():
    unfitted_sax = SymbolicAggregateApproximation(n_segments=3,
                                                  alphabet_size_avg=2)
    data = [[-1., 2., 0.1, -1., 1., -1.], [1., 3.2, -1., -3., 1., -1.]]
    np.testing.assert_raises(ValueError, unfitted_sax.distance,
                             data[0], data[1])


def test_1dsax():
    unfitted_1dsax = OneD_SymbolicAggregateApproximation(n_segments=3,
                                                         alphabet_size_avg=2,
                                                         alphabet_size_slope=2)
    data = [[-1., 2., 0.1, -1., 1., -1.], [1., 3.2, -1., -3., 1., -1.]]
    np.testing.assert_raises(ValueError, unfitted_1dsax.distance,
                             data[0], data[1])