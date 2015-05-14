from copy import copy
import unittest

from django.test import TestCase
from wms.tests import add_server, add_group, add_user, add_dataset, image_path
from wms.models import Dataset, SGridDataset


@unittest.skip("SGRID Datasets are not implemented yet")
class TestSgrid(TestCase):

    @classmethod
    def setUpClass(cls):
        add_server()
        add_group()
        add_user()
        add_dataset("sgrid_testing", "sgrid", "coawst_sgrid.nc")

    @classmethod
    def tearDownClass(cls):
        d = Dataset.objects.get(name="sgrid_testing")
        d.clear_cache()
        d.delete()

    def setUp(self):
        self.dataset_name = 'sgrid_testing'
        self.url_params = dict(
            service     = 'WMS',
            request     = 'GetMap',
            version     = '1.1.1',
            layers      = 'u',
            format      = 'image/png',
            transparent = 'true',
            height      = 256,
            width       = 256,
            srs         = 'EPSG:3857',
            bbox        = '-8140237.76425813,4852834.051769271,-7983694.730330088,5009377.085697313'
        )

    def image_name(self):
        return '{}.png'.format(self.id().split('.')[-1])

    def test_identify(self):
        d = Dataset.objects.get(name=self.dataset_name)
        klass = Dataset.identify(d.uri)
        assert klass == SGridDataset

    @unittest.skip("filledcontours is not yet implemeted for SGRID datasets")
    def test_filledcontours(self):
        params = copy(self.url_params)
        params.update(styles='filledcontours_jet')
        response = self.client.get('/wms/datasets/{}'.format(self.dataset_name), params)
        self.assertEqual(response.status_code, 200)
        with open(image_path(self.__class__.__name__, self.image_name()), "wb") as f:
            f.write(response.content)

    @unittest.skip("facets is not yet implemeted for SGRID datasets")
    def test_facets(self):
        params = copy(self.url_params)
        params.update(styles='facets_jet')
        response = self.client.get('/wms/datasets/{}'.format(self.dataset_name), params)
        self.assertEqual(response.status_code, 200)
        with open(image_path(self.__class__.__name__, self.image_name()), "wb") as f:
            f.write(response.content)

    @unittest.skip("pcolor is not yet implemeted for SGRID datasets")
    def test_pcolor(self):
        params = copy(self.url_params)
        params.update(styles='pcolor_jet')
        response = self.client.get('/wms/datasets/{}'.format(self.dataset_name), params)
        self.assertEqual(response.status_code, 200)
        with open(image_path(self.__class__.__name__, self.image_name()), "wb") as f:
            f.write(response.content)

    @unittest.skip("contours is not yet implemeted for SGRID datasets")
    def test_contours(self):
        params = copy(self.url_params)
        params.update(styles='contours_jet')
        response = self.client.get('/wms/datasets/{}'.format(self.dataset_name), params)
        self.assertEqual(response.status_code, 200)
        with open(image_path(self.__class__.__name__, self.image_name()), "wb") as f:
            f.write(response.content)

    @unittest.skip("vectors is not yet implemeted for SGRID datasets")
    def test_vectors(self):
        params = copy(self.url_params)
        params.update(styles='vectors_jet', layers='u,v')
        response = self.client.get('/wms/datasets/{}'.format(self.dataset_name), params)
        self.assertEqual(response.status_code, 200)
        with open(image_path(self.__class__.__name__, self.image_name()), "wb") as f:
            f.write(response.content)

    def test_getCaps(self):
        params = dict(request='GetCapabilities')
        response = self.client.get('/wms/datasets/{}'.format(self.dataset_name), params)
        self.assertEqual(response.status_code, 200)

    def test_create_layers(self):
        d = Dataset.objects.get(name=self.dataset_name)
        assert d.layer_set.count() == 12
