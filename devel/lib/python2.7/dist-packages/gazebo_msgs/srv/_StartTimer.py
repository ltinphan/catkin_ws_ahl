# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gazebo_msgs/StartTimerRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class StartTimerRequest(genpy.Message):
  _md5sum = "8ff7d44c34992c271801e5f640dcfa8d"
  _type = "gazebo_msgs/StartTimerRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 duration_write_joint_states
float64 duration_update_link_states
float64 duration_read_joint_efforts
float64 duration_write_forces

"""
  __slots__ = ['duration_write_joint_states','duration_update_link_states','duration_read_joint_efforts','duration_write_forces']
  _slot_types = ['float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       duration_write_joint_states,duration_update_link_states,duration_read_joint_efforts,duration_write_forces

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StartTimerRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.duration_write_joint_states is None:
        self.duration_write_joint_states = 0.
      if self.duration_update_link_states is None:
        self.duration_update_link_states = 0.
      if self.duration_read_joint_efforts is None:
        self.duration_read_joint_efforts = 0.
      if self.duration_write_forces is None:
        self.duration_write_forces = 0.
    else:
      self.duration_write_joint_states = 0.
      self.duration_update_link_states = 0.
      self.duration_read_joint_efforts = 0.
      self.duration_write_forces = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4d.pack(_x.duration_write_joint_states, _x.duration_update_link_states, _x.duration_read_joint_efforts, _x.duration_write_forces))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.duration_write_joint_states, _x.duration_update_link_states, _x.duration_read_joint_efforts, _x.duration_write_forces,) = _struct_4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4d.pack(_x.duration_write_joint_states, _x.duration_update_link_states, _x.duration_read_joint_efforts, _x.duration_write_forces))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 32
      (_x.duration_write_joint_states, _x.duration_update_link_states, _x.duration_read_joint_efforts, _x.duration_write_forces,) = _struct_4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d = struct.Struct("<4d")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gazebo_msgs/StartTimerResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class StartTimerResponse(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "gazebo_msgs/StartTimerResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StartTimerResponse, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
class StartTimer(object):
  _type          = 'gazebo_msgs/StartTimer'
  _md5sum = '8ff7d44c34992c271801e5f640dcfa8d'
  _request_class  = StartTimerRequest
  _response_class = StartTimerResponse