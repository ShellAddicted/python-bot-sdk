# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from . import definitions_pb2 as definitions__pb2
from . import miscellaneous_pb2 as miscellaneous__pb2
from dialog_api.scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='device_info.proto',
  package='dialog',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x64\x65vice_info.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x13miscellaneous.proto\x1a\x15scalapb/scalapb.proto\"\xa8\x01\n\x1cRequestNotifyAboutDeviceInfo\x12*\n\x13preferred_languages\x18\x01 \x03(\tB\r\x8a\xea\x30\t\n\x07visible\x12>\n\ttime_zone\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"\xf8\x02\n\nClientInfo\x12\x35\n\x08platform\x18\x01 \x01(\x0e\x32\x14.dialog.PlatformTypeB\r\x8a\xea\x30\t\n\x07visible\x12\"\n\x0b\x64\x65vice_name\x18\x02 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x1f\n\x08\x61pp_name\x18\x03 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12@\n\x0b\x61pp_version\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible\x12@\n\x0bsdk_version\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible\x12*\n\x13preferred_languages\x18\x06 \x03(\tB\r\x8a\xea\x30\t\n\x07visible\x12>\n\ttime_zone\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible*\x9c\x01\n\x0cPlatformType\x12\x18\n\x14PLATFORMTYPE_UNKNOWN\x10\x00\x12\x18\n\x14PLATFORMTYPE_ANDROID\x10\x01\x12\x14\n\x10PLATFORMTYPE_IOS\x10\x02\x12\x14\n\x10PLATFORMTYPE_WEB\x10\x03\x12\x14\n\x10PLATFORMTYPE_CLC\x10\x04\x12\x16\n\x12PLATFORMTYPE_TESTS\x10*2\x98\x01\n\nDeviceInfo\x12\x89\x01\n\x15NotifyAboutDeviceInfo\x12$.dialog.RequestNotifyAboutDeviceInfo\x1a\x14.dialog.ResponseVoid\"4\x82\xd3\xe4\x93\x02.\")/v1/grpc/DeviceInfo/NotifyAboutDeviceInfo:\x01*B\x19\xe2?\x16\n\x14im.dlg.grpc.servicesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,miscellaneous__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])

_PLATFORMTYPE = _descriptor.EnumDescriptor(
  name='PlatformType',
  full_name='dialog.PlatformType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLATFORMTYPE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORMTYPE_ANDROID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORMTYPE_IOS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORMTYPE_WEB', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORMTYPE_CLC', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORMTYPE_TESTS', index=5, number=42,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=705,
  serialized_end=861,
)
_sym_db.RegisterEnumDescriptor(_PLATFORMTYPE)

PlatformType = enum_type_wrapper.EnumTypeWrapper(_PLATFORMTYPE)
PLATFORMTYPE_UNKNOWN = 0
PLATFORMTYPE_ANDROID = 1
PLATFORMTYPE_IOS = 2
PLATFORMTYPE_WEB = 3
PLATFORMTYPE_CLC = 4
PLATFORMTYPE_TESTS = 42



_REQUESTNOTIFYABOUTDEVICEINFO = _descriptor.Descriptor(
  name='RequestNotifyAboutDeviceInfo',
  full_name='dialog.RequestNotifyAboutDeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='preferred_languages', full_name='dialog.RequestNotifyAboutDeviceInfo.preferred_languages', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_zone', full_name='dialog.RequestNotifyAboutDeviceInfo.time_zone', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=323,
)


_CLIENTINFO = _descriptor.Descriptor(
  name='ClientInfo',
  full_name='dialog.ClientInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform', full_name='dialog.ClientInfo.platform', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='dialog.ClientInfo.device_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='dialog.ClientInfo.app_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_version', full_name='dialog.ClientInfo.app_version', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sdk_version', full_name='dialog.ClientInfo.sdk_version', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preferred_languages', full_name='dialog.ClientInfo.preferred_languages', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_zone', full_name='dialog.ClientInfo.time_zone', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=702,
)

_REQUESTNOTIFYABOUTDEVICEINFO.fields_by_name['time_zone'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLIENTINFO.fields_by_name['platform'].enum_type = _PLATFORMTYPE
_CLIENTINFO.fields_by_name['app_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLIENTINFO.fields_by_name['sdk_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CLIENTINFO.fields_by_name['time_zone'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['RequestNotifyAboutDeviceInfo'] = _REQUESTNOTIFYABOUTDEVICEINFO
DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
DESCRIPTOR.enum_types_by_name['PlatformType'] = _PLATFORMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestNotifyAboutDeviceInfo = _reflection.GeneratedProtocolMessageType('RequestNotifyAboutDeviceInfo', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTNOTIFYABOUTDEVICEINFO,
  __module__ = 'device_info_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestNotifyAboutDeviceInfo)
  ))
_sym_db.RegisterMessage(RequestNotifyAboutDeviceInfo)

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTINFO,
  __module__ = 'device_info_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ClientInfo)
  ))
_sym_db.RegisterMessage(ClientInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\342?\026\n\024im.dlg.grpc.services'))
_REQUESTNOTIFYABOUTDEVICEINFO.fields_by_name['preferred_languages'].has_options = True
_REQUESTNOTIFYABOUTDEVICEINFO.fields_by_name['preferred_languages']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_REQUESTNOTIFYABOUTDEVICEINFO.fields_by_name['time_zone'].has_options = True
_REQUESTNOTIFYABOUTDEVICEINFO.fields_by_name['time_zone']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_REQUESTNOTIFYABOUTDEVICEINFO.has_options = True
_REQUESTNOTIFYABOUTDEVICEINFO._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\342?\031\n\027im.dlg.grpc.GrpcRequest'))
_CLIENTINFO.fields_by_name['platform'].has_options = True
_CLIENTINFO.fields_by_name['platform']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_CLIENTINFO.fields_by_name['device_name'].has_options = True
_CLIENTINFO.fields_by_name['device_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_CLIENTINFO.fields_by_name['app_name'].has_options = True
_CLIENTINFO.fields_by_name['app_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_CLIENTINFO.fields_by_name['app_version'].has_options = True
_CLIENTINFO.fields_by_name['app_version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_CLIENTINFO.fields_by_name['sdk_version'].has_options = True
_CLIENTINFO.fields_by_name['sdk_version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_CLIENTINFO.fields_by_name['preferred_languages'].has_options = True
_CLIENTINFO.fields_by_name['preferred_languages']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))
_CLIENTINFO.fields_by_name['time_zone'].has_options = True
_CLIENTINFO.fields_by_name['time_zone']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3520\t\n\007visible'))

_DEVICEINFO = _descriptor.ServiceDescriptor(
  name='DeviceInfo',
  full_name='dialog.DeviceInfo',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=864,
  serialized_end=1016,
  methods=[
  _descriptor.MethodDescriptor(
    name='NotifyAboutDeviceInfo',
    full_name='dialog.DeviceInfo.NotifyAboutDeviceInfo',
    index=0,
    containing_service=None,
    input_type=_REQUESTNOTIFYABOUTDEVICEINFO,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002.\")/v1/grpc/DeviceInfo/NotifyAboutDeviceInfo:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_DEVICEINFO)

DESCRIPTOR.services_by_name['DeviceInfo'] = _DEVICEINFO

# @@protoc_insertion_point(module_scope)
