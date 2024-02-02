import configparser
import os

from square_logger.main import SquareLogger

from lapa_commons import MODULE_NAME

global_object_square_logger = SquareLogger(MODULE_NAME)


def read_configuration_from_file_path(pstr_file_path: str) -> dict:
    """
    Description: This function is used to validate whether the pstr_file_path exists or not.
    If path exists -> Call read_configuration() function.
    If path does not exist -> Log error and return empty dictionary.

    :param pstr_file_path: path of the configuration file.
    :return: dictionary containing the output as key-value pair.
    """
    try:
        ldict_configuration_variables = dict()
        # ====================================================================
        # Validate the datatype of pstr_file_path
        # ====================================================================
        if not isinstance(pstr_file_path, str):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pstr_file_path.'
                f' Received datatype - {str(type(pstr_file_path))}, Expected datatype - str.', exc_info=True)
            return ldict_configuration_variables

        # ====================================================================
        # Check if the file path exists
        # ====================================================================
        if os.path.exists(pstr_file_path):
            return read_configuration(pstr_file_path)
        else:
            global_object_square_logger.logger.error(f'File does not exists. File path - {str(pstr_file_path)}',
                                                     exc_info=True)
            raise
    except Exception:
        raise


def read_configuration(pstr_file_path: str) -> dict:
    """
    Description: This function is used to read the configuration file.

    :param pstr_file_path: path of the configuration file.
    :return: dictionary containing the output as key-value pair.
    :example: {'Env_One': 'One', 'Env_Three': 'Three', 'Env_Two': 'Two'}
    """
    try:
        ldict_configuration_variables = dict()

        # ====================================================================
        # Use of RawConfigParser and optionxform=str to preserve the case of variables.
        # configparser by default will convert everything to lowercase.
        # ====================================================================
        lobj_configparser = configparser.RawConfigParser()
        lobj_configparser.optionxform = str
        lobj_configparser.read(pstr_file_path)
        llst_configuration_sections = lobj_configparser.sections()

        # ====================================================================
        # Iterate over each configuration section
        # ====================================================================
        for lstr_configuration_section in llst_configuration_sections:
            # ====================================================================
            # If the configuration section is environment call read_environment_configuration_variables()
            # ====================================================================
            if lstr_configuration_section.lower() == 'environment':
                llst_environment_variables = lobj_configparser.options(lstr_configuration_section)
                ldict_configuration_variables = read_environment_configuration_variables(
                    lobj_configparser, lstr_configuration_section, llst_environment_variables,
                    ldict_configuration_variables)
            else:
                # ====================================================================
                # Read the configuration section using read_configuration_variables() function
                # ====================================================================
                llst_configuration_variables = lobj_configparser.options(lstr_configuration_section)
                ldict_configuration_variables = read_configuration_variables(
                    lobj_configparser, lstr_configuration_section, llst_configuration_variables,
                    ldict_configuration_variables)
        return ldict_configuration_variables
    except Exception:
        raise
    finally:
        del lobj_configparser


def read_configuration_variables(pobj_configparser: object,
                                 pstr_configuration_section: str,
                                 plst_configuration_variables: list,
                                 pdict_configuration_variables: dict) -> dict:
    """
    Description: This function is used to read the configuration variables for a particular section.

    :param pobj_configparser: configparser object
    :param pstr_configuration_section: section of the configuration file
    :param plst_configuration_variables: list of configuration variables
    :param pdict_configuration_variables: output dictionary which will contain all the key-value pair
    :return: pdict_configuration_variables
    """
    try:
        if not isinstance(pobj_configparser, object):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pobj_configparser.'
                f' Received datatype - {str(type(pobj_configparser))}, Expected datatype - object.', exc_info=True)
            raise

        if not isinstance(pstr_configuration_section, str):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pstr_configuration_section.'
                f' Received datatype - {str(type(pstr_configuration_section))}, Expected datatype - str.',
                exc_info=True)
            raise

        if not isinstance(plst_configuration_variables, list):
            global_object_square_logger.logger.error(
                'Invalid datatype received for plst_configuration_variables.'
                f' Received datatype - {str(type(plst_configuration_variables))}, Expected datatype - list.',
                exc_info=True)
            raise

        if not isinstance(pdict_configuration_variables, dict):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pdict_configuration_variables.'
                f' Received datatype - {str(type(pdict_configuration_variables))}, Expected datatype - dict.',
                exc_info=True)
            raise

        for lstr_configuration_variable in plst_configuration_variables:
            pdict_configuration_variables[lstr_configuration_variable] = read_configuration_using_configparser(
                pobj_configparser, pstr_configuration_section, lstr_configuration_variable)
        return pdict_configuration_variables
    except Exception:
        raise


def read_environment_configuration_variables(pobj_configparser: object,
                                             pstr_configuration_section: str,
                                             plst_environment_variables: list,
                                             pdict_configuration_variables: dict) -> dict:
    """
    Description: This function is used to read the configuration variables for an environment section.
    It will first check if the environment variables exists in the OS.
    If found --> Read the value from the OS.
    If not found --> Read from the configuration file.

    :param pobj_configparser: configparser object.
    :param pstr_configuration_section: section of the configuration file.
    :param plst_environment_variables: list of configuration variables.
    :param pdict_configuration_variables: output dictionary which will contain all the key-value pair.
    :return: pdict_configuration_variables
    """
    try:
        if not isinstance(pobj_configparser, object):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pobj_configparser.'
                f' Received datatype - {str(type(pobj_configparser))}, Expected datatype - object.', exc_info=True)
            raise

        if not isinstance(pstr_configuration_section, object):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pstr_configuration_section.'
                f' Received datatype - {str(type(pstr_configuration_section))}, Expected datatype - str.',
                exc_info=True)
            raise

        if not isinstance(plst_environment_variables, object):
            global_object_square_logger.logger.error(
                'Invalid datatype received for plst_environment_variables.'
                f' Received datatype - {str(type(plst_environment_variables))}, Expected datatype - list.',
                exc_info=True)
            raise

        if not isinstance(pdict_configuration_variables, object):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pdict_configuration_variables.'
                f' Received datatype - {str(type(pdict_configuration_variables))}, Expected datatype - dict.',
                exc_info=True)
            raise

        for lstr_environment_variable in plst_environment_variables:
            lstr_environment_variable_os_value = os.environ.get(lstr_environment_variable)
            if lstr_environment_variable_os_value is not None:
                # ====================================================================
                # Environment variable found in the OS
                # ====================================================================
                pdict_configuration_variables[lstr_environment_variable] = lstr_environment_variable_os_value
            else:
                # ====================================================================
                # Environment variable not found in the OS, reading from the configuration file
                # ====================================================================
                pdict_configuration_variables[lstr_environment_variable] = read_configuration_using_configparser(
                    pobj_configparser, pstr_configuration_section, lstr_environment_variable)
        return pdict_configuration_variables
    except Exception:
        raise


def read_configuration_using_configparser(pobj_configparser: object,
                                          pstr_configuration_section: str,
                                          pstr_variable_name: str):
    """
    Description: This function is used to read the configuration variable from the section with the help of
    configparser.

    :param pobj_configparser: configparser object
    :param pstr_configuration_section: section of the configuration file
    :param pstr_variable_name: variable name from the configuration file
    """
    try:
        if not isinstance(pobj_configparser, object):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pobj_configparser.'
                f' Received datatype - {str(type(pobj_configparser))}, Expected datatype - object.', exc_info=True)
            raise

        if not isinstance(pstr_configuration_section, object):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pstr_configuration_section.'
                f' Received datatype - {str(type(pstr_configuration_section))}, Expected datatype - str.',
                exc_info=True)
            raise

        if not isinstance(pstr_variable_name, object):
            global_object_square_logger.logger.error(
                'Invalid datatype received for pstr_variable_name.'
                f' Received datatype - {str(type(pstr_variable_name))}, Expected datatype - str.', exc_info=True)
            raise

        return pobj_configparser.get(pstr_configuration_section, pstr_variable_name)
    except Exception:
        raise
