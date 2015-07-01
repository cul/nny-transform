import unittest
import difflib
import wwwapp
import re
import os
class TestWwwAppMethods(unittest.TestCase):
  def normalize(self,src):
    src = src.replace("\t",' ')
    src = src.replace("</br>",'')
    src = src.replace("</hr>",'')
    src = src.replace("</meta>",'')
    src = re.sub(r'\s+',' ',src)
    return src
  def ignorable(self,line):
    line = re.sub(r'[+-]\s*$','  ',line)
    return line if re.match(r'[+-]\s(.*)$',line) else ''
  def assertMultiLineEqual(self, expected, actual, msg=None):
    """Assert that two multi-line strings are equal or fail with a diff
       Normalize some HTML nonsense
    """
    self.assertTrue(isinstance(expected, str),
            'Expected argument is not a string')
    self.assertTrue(isinstance(actual, str),
            'Actual argument is not a string')
    expected = map(self.normalize,open(expected, 'r').readlines())

    actual = map(self.normalize,open(actual,'r').readlines())
    diff = map(self.ignorable,difflib.ndiff(expected,actual))
    message = ''.join(diff)
    if len(message) > 0:
      message = "\n".join(diff)
      if msg:
        message += " : " + msg
      self.fail("Multi-line strings are unequal:\n" + message)

  def test_transform_action(self):
    input = wwwapp.WWWAPP_URL
    expected = wwwapp.FULLTEXT_URL
    rig = wwwapp.Transformer()
    actual = rig.transform_action(input)
    self.assertEqual(expected, actual)
    input = "http://something.info"
    actual = rig.transform_action(input)
    self.assertEqual(False, actual)

  def test_Transformer(self):
    rig = wwwapp.Transformer()
    fixture = "fixtures/test/input/audio_transcript.html"
    expected = "fixtures/test/expected/audio_transcript.html"
    actual = "tmp/audio_transcript.html"
    rig.transform(fixture,actual)
    normal_expect = "tmp/expected.html"
    rig.transform(expected,normal_expect)
    self.assertMultiLineEqual(normal_expect,actual)

  def test_Transformer_directories(self):
    rig = wwwapp.Transformer()
    fixture = "fixtures/test/input"
    expected = "fixtures/test/expected/audio_transcript.html"
    actual = "tmp/audio_transcript.html"
    rig.transform(fixture,"tmp")
    normal_expect = "tmp/expected.html"
    rig.transform(expected,normal_expect)
    self.assertMultiLineEqual(normal_expect,actual)

if __name__ == '__main__':
  unittest.main()