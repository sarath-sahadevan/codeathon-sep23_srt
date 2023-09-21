def is_valid_ip_address(ip):
    try:
        # Split the IP address into its components
        components = ip.split('.')
        
        # Check that there are exactly 4 components
        if len(components) != 4:
            return False
        
        # Check that each component is an integer between 0 and 255
        for component in components:
            value = int(component)
            if value < 0 or value > 255:
                return False
        
        return True
    except ValueError:
        return False


import unittest

class TestIsValidIPAddress(unittest.TestCase):
    def test_valid_ip(self):
        self.assertTrue(is_valid_ip_address('192.168.0.1'))
    
    def test_invalid_ip(self):
        self.assertFalse(is_valid_ip_address('256.0.0.1'))
    
    def test_missing_components(self):
        self.assertFalse(is_valid_ip_address('192.168.1'))
    
    def test_extra_components(self):
        self.assertFalse(is_valid_ip_address('192.168.0.1.1'))
    
    def test_non_numeric_components(self):
        self.assertFalse(is_valid_ip_address('192.168.0.a'))
    
if __name__ == '__main__':
    unittest.main()