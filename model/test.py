import unittest
from api.database import get_credentials

class Test(unittest.TestCase):
    credentials = get_credentials()

    # def test_upload_file_imageKit(self):
    #     from imageKit_api import upload_file_imageKit

    #     response = upload_file_imageKit('../test_image.png', self.credentials)
    #     self.assertEqual(response['versionInfo']['name'], 'Version 1')

    # def test_read_image(self):
    #     from azure_api import read_image

    #     result = read_image('../data/1_1.png', self.credentials)
    #     self.assertIn('6.35686-01-1', result)

    # def test_search_data(self):
    #     from preprocessing import search_data


    #     data = "DECCA STEREO Direct Metal ®0 Dmm Mastering 6.35686-1 6.35686-01-1 00 TELDEC (414 423-1) DIGITAL RECORDING SPEED 3313 Contr. Copyr D & C 1985 GEORG FRIEDRICH HÄNDEL (1685-1759) Esther Overture - Scenes I + II Andrew King - David Thomas - Paul Elliott - Emma Kirkby Westminster Cathedral Boy's Choir Chor und Orchester der Academy of Ancient Music Leitung: Christopher Hogwood LAUBTE VERVIELFALTIGUNG VERMIETUNG AUFFUI"
    #     result = search_data(data)
    #     self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()