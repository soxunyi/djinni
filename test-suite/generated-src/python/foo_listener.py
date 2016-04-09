# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from foo_listener.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyBinary, CPyBoxedI32, CPyDate, CPyPrimitive, CPyRecord, CPyString

from abc import ABCMeta, abstractmethod
from foo_some_other_record import FooSomeOtherRecord
from foo_some_other_record_helper import FooSomeOtherRecordHelper
from future.utils import with_metaclass
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class FooListener(with_metaclass(ABCMeta)):
    @abstractmethod
    def on_string_change(self, private_string):
        raise NotImplementedError

    @abstractmethod
    def get_private_int(self):
        raise NotImplementedError

    @abstractmethod
    def on_changes_string_returned(self, i, f, s, binar, b, d):
        raise NotImplementedError

    @abstractmethod
    def on_changes_binary_returned(self, i, f, s, binar, b, d):
        raise NotImplementedError

    @abstractmethod
    def on_changes_date_returned(self, i, f, s, binar, b, d):
        raise NotImplementedError

    @abstractmethod
    def on_changes_int_returned(self, i, f, s, binar, b, d):
        raise NotImplementedError

    @abstractmethod
    def on_changes_record_returned(self, n1, n2):
        raise NotImplementedError

    @abstractmethod
    def on_changes_string_optional_returned(self, i, f, s, binar, b, d):
        raise NotImplementedError

    @abstractmethod
    def on_changes_int_optional_returned(self, i, f, s, binar, b, d):
        raise NotImplementedError

    @abstractmethod
    def cause_py_exception(self, exception_arg):
        raise NotImplementedError

    @abstractmethod
    def cause_zero_division_error(self):
        raise NotImplementedError


class FooListenerCallbacksHelper():
    @ffi.callback("struct DjinniString *(struct DjinniObjectHandle * , struct DjinniString *)")
    def on_string_change(cself, private_string):
        try:
            with CPyString.fromPy(FooListenerHelper.selfToPy(cself).on_string_change(CPyString.toPy(private_string))) as py_obj:
                _ret = py_obj.release_djinni_string()
                assert _ret != ffi.NULL
                return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int32_t(struct DjinniObjectHandle * )")
    def get_private_int(cself):
        try:
            _ret = CPyPrimitive.fromPy(FooListenerHelper.selfToPy(cself).get_private_int())
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniString *(struct DjinniObjectHandle * , int32_t, float, struct DjinniString *, struct DjinniBinary *, bool, uint64_t)")
    def on_changes_string_returned(cself, i, f, s, binar, b, d):
        try:
            with CPyString.fromPy(FooListenerHelper.selfToPy(cself).on_changes_string_returned(CPyPrimitive.toPy(i), CPyPrimitive.toPy(f), CPyString.toPy(s), CPyBinary.toPy(binar), CPyPrimitive.toPy(b), CPyDate.toPy(d))) as py_obj:
                _ret = py_obj.release_djinni_string()
                assert _ret != ffi.NULL
                return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBinary *(struct DjinniObjectHandle * , int32_t, float, struct DjinniString *, struct DjinniBinary *, bool, uint64_t)")
    def on_changes_binary_returned(cself, i, f, s, binar, b, d):
        try:
            with CPyBinary.fromPy(FooListenerHelper.selfToPy(cself).on_changes_binary_returned(CPyPrimitive.toPy(i), CPyPrimitive.toPy(f), CPyString.toPy(s), CPyBinary.toPy(binar), CPyPrimitive.toPy(b), CPyDate.toPy(d))) as py_obj:
                _ret = py_obj.release_djinni_binary()
                assert _ret != ffi.NULL
                return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("uint64_t(struct DjinniObjectHandle * , int32_t, float, struct DjinniString *, struct DjinniBinary *, bool, uint64_t)")
    def on_changes_date_returned(cself, i, f, s, binar, b, d):
        try:
            _ret = CPyDate.fromPy(FooListenerHelper.selfToPy(cself).on_changes_date_returned(CPyPrimitive.toPy(i), CPyPrimitive.toPy(f), CPyString.toPy(s), CPyBinary.toPy(binar), CPyPrimitive.toPy(b), CPyDate.toPy(d)))
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("int32_t(struct DjinniObjectHandle * , int32_t, float, struct DjinniString *, struct DjinniBinary *, bool, uint64_t)")
    def on_changes_int_returned(cself, i, f, s, binar, b, d):
        try:
            _ret = CPyPrimitive.fromPy(FooListenerHelper.selfToPy(cself).on_changes_int_returned(CPyPrimitive.toPy(i), CPyPrimitive.toPy(f), CPyString.toPy(s), CPyBinary.toPy(binar), CPyPrimitive.toPy(b), CPyDate.toPy(d)))
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(struct DjinniObjectHandle * , int32_t, int32_t)")
    def on_changes_record_returned(cself, n1, n2):
        try:
            _ret = CPyRecord.fromPy(FooSomeOtherRecord.c_data_set, FooListenerHelper.selfToPy(cself).on_changes_record_returned(CPyPrimitive.toPy(n1), CPyPrimitive.toPy(n2)))
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniString *(struct DjinniObjectHandle * , struct DjinniBoxedI32 *, float, struct DjinniString *, struct DjinniBinary *, int32_t, uint64_t)")
    def on_changes_string_optional_returned(cself, i, f, s, binar, b, d):
        try:
            with CPyString.fromPyOpt(FooListenerHelper.selfToPy(cself).on_changes_string_optional_returned(CPyBoxedI32.toPyOpt(i), CPyPrimitive.toPy(f), CPyString.toPyOpt(s), CPyBinary.toPy(binar), CPyPrimitive.toPy(b), CPyDate.toPy(d))) as py_obj:
                return py_obj.release_djinni_string()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniBoxedI32 *(struct DjinniObjectHandle * , struct DjinniBoxedI32 *, float, struct DjinniString *, struct DjinniBinary *, int32_t, uint64_t)")
    def on_changes_int_optional_returned(cself, i, f, s, binar, b, d):
        try:
            with CPyBoxedI32.fromPyOpt(FooListenerHelper.selfToPy(cself).on_changes_int_optional_returned(CPyBoxedI32.toPyOpt(i), CPyPrimitive.toPy(f), CPyString.toPyOpt(s), CPyBinary.toPy(binar), CPyPrimitive.toPy(b), CPyDate.toPy(d))) as py_obj:
                return py_obj.release_djinni_boxed()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("void(struct DjinniObjectHandle * , struct DjinniString *)")
    def cause_py_exception(cself, exception_arg):
        try:
            FooListenerHelper.selfToPy(cself).cause_py_exception(CPyString.toPy(exception_arg))
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)

    @ffi.callback("void(struct DjinniObjectHandle * )")
    def cause_zero_division_error(cself):
        try:
            FooListenerHelper.selfToPy(cself).cause_zero_division_error()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)

    @ffi.callback("void(struct DjinniObjectHandle * )")
    def __delete(c_ptr):
        assert c_ptr in FooListenerHelper.c_data_set
        FooListenerHelper.c_data_set.remove(c_ptr)

    @staticmethod
    def _add_callbacks():
        lib.foo_listener_add_callback_on_string_change(FooListenerCallbacksHelper.on_string_change)
        lib.foo_listener_add_callback_get_private_int(FooListenerCallbacksHelper.get_private_int)
        lib.foo_listener_add_callback_on_changes_string_returned(FooListenerCallbacksHelper.on_changes_string_returned)
        lib.foo_listener_add_callback_on_changes_binary_returned(FooListenerCallbacksHelper.on_changes_binary_returned)
        lib.foo_listener_add_callback_on_changes_date_returned(FooListenerCallbacksHelper.on_changes_date_returned)
        lib.foo_listener_add_callback_on_changes_int_returned(FooListenerCallbacksHelper.on_changes_int_returned)
        lib.foo_listener_add_callback_on_changes_record_returned(FooListenerCallbacksHelper.on_changes_record_returned)
        lib.foo_listener_add_callback_on_changes_string_optional_returned(FooListenerCallbacksHelper.on_changes_string_optional_returned)
        lib.foo_listener_add_callback_on_changes_int_optional_returned(FooListenerCallbacksHelper.on_changes_int_optional_returned)
        lib.foo_listener_add_callback_cause_py_exception(FooListenerCallbacksHelper.cause_py_exception)
        lib.foo_listener_add_callback_cause_zero_division_error(FooListenerCallbacksHelper.cause_zero_division_error)

        lib.foo_listener_add_callback___delete(FooListenerCallbacksHelper.__delete)

FooListenerCallbacksHelper._add_callbacks()

class FooListenerHelper:
    c_data_set = MultiSet()
    @staticmethod
    def toPy(obj):
        if obj == ffi.NULL:
            return None
        # Python Objects can be returned without being wrapped in proxies
        py_handle = lib.get_handle_from_proxy_object_cw__foo_listener(obj)
        if py_handle:
            assert py_handle in FooListenerHelper.c_data_set
            aux = ffi.from_handle(ffi.cast("void * ", py_handle))
            lib.foo_listener___wrapper_dec_ref(obj)
            return aux
        return FooListenerCppProxy(obj)

    @staticmethod
    def selfToPy(obj):
        assert obj in FooListenerHelper.c_data_set
        return ffi.from_handle(ffi.cast("void * ",obj))

    @staticmethod
    def fromPy(py_obj):
        if py_obj is None:
            return ffi.NULL
        py_proxy = (py_obj)
        if not hasattr(py_obj, "on_string_change"):
            raise TypeError
        if not hasattr(py_obj, "get_private_int"):
            raise TypeError
        if not hasattr(py_obj, "on_changes_string_returned"):
            raise TypeError
        if not hasattr(py_obj, "on_changes_binary_returned"):
            raise TypeError
        if not hasattr(py_obj, "on_changes_date_returned"):
            raise TypeError
        if not hasattr(py_obj, "on_changes_int_returned"):
            raise TypeError
        if not hasattr(py_obj, "on_changes_record_returned"):
            raise TypeError
        if not hasattr(py_obj, "on_changes_string_optional_returned"):
            raise TypeError
        if not hasattr(py_obj, "on_changes_int_optional_returned"):
            raise TypeError
        if not hasattr(py_obj, "cause_py_exception"):
            raise TypeError
        if not hasattr(py_obj, "cause_zero_division_error"):
            raise TypeError

        bare_c_ptr = ffi.new_handle(py_proxy)
        FooListenerHelper.c_data_set.add(bare_c_ptr)
        wrapped_c_ptr = lib.make_proxy_object_from_handle_cw__foo_listener(bare_c_ptr)
        return wrapped_c_ptr