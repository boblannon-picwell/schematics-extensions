import pytest

from schematics.types import StringType
from schematics.types.compound import ModelType, ListType
from schematics.models import Model

from ..mockable_list_type import MockableListType
from ..mockable_model_type import MockableModelType


class ExampleSubmodel(Model):
    attribute = StringType(required=True, min_length=10, max_length=10)


class ExampleModel(Model):
    submodels = MockableListType(MockableModelType(ExampleSubmodel), required=True)


class ExampleModelWithStrings(Model):
    strings = MockableListType(StringType(min_length=10, max_length=10), required=True)


def test_mockable_list_type_attribute_generates_a_list_of_mocked_models():
    model = ExampleModel.get_mock_object()
    submodel = model.submodels[0]
    assert type(submodel) == ExampleSubmodel
    assert len(submodel.attribute) == 10


def test_mockable_list_type_attribute_works_with_builtin_simple_types():
    model = ExampleModelWithStrings.get_mock_object()
    first_string = model.strings[0]
    assert len(first_string) == 10
