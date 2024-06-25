Feature: Test Feature

  @test_run
  Scenario Outline: Test Scenario
    Given User is preparing to test <keyword>
    When test_step_2
    Then test_step_3

    Examples:
    |keyword|
    |test_1 |