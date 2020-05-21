# README:

## Goals:
- Goals are state definitions - they use *Stative verbs*: Be, have, understand. Goals satisfy X-condition by Y date.
- https://en.wikipedia.org/wiki/Stative_verb
- Goals can be broken
- Actions are performed to transition from current state to goal state - they are *Dynamic verbs*

## Actions
- Actions are performed every period until the desired metric is reached.
- https://en.wikipedia.org/wiki/Dynamic_verb
- Actions are related to Intentions and Measurements.

## Intentions:
- Intentions are daily commitments to carry out the action, with metrics to track progress.

#  Measurements:
- Measurements record the outcome of your Intentions. Each is associated with an Action, and a Measurement.

### Examples:
If you wanted to maintain your level of something, you would set an Action with the verb 'maintain'.
 
If you wanted to reach a state, and then maintain it, you would first create an Action with the verb 'increase',
then once the target metric on that is reached, create a 'maintain' action, and continue.

#### Form for thinking about actions:
- Action Verb + Metric Name + Target (+ Unit) 
- Reduce + Calorie intake + to 2000kcal
- Increase + Squat weight + to 70kg/Squat
- Maintain + Meditation time + at 40mins
- Reduce + Expenditures + to £50,000
- Increase + Savings + to £50,000
- Maintain + Net Worth + at £50,000


# Server:
- REWRITE FOR PYTHON 3



#Client:
- Add custom menu
    - Nestable menu items
    - Custom menu items
    - switch menu based on selection of module
- titles on each list
- Customise forms
    - Fields showing parent ids should be ReferenceFields enclosing TextFields
    - Expand datagrid rows for sub-views (eg subgoals on goaledit)
- Create Dashboard with chart allowing selection of goal, then shows Progress, and intention alignment
- make all datagrid rows clickable
- make all datagrid rows expandable

#MODULES:
- Achievement
    - Subgoal refactoring
        - Goals List to show only goals with no parent?
        - Parent autocompletion service?
    - Goal Edit
        - Fix bug: some sorts on Subgoals dont work
    - clickable datagrid rows on all edit views
        - https://marmelab.com/react-admin/List.html#the-datagrid-component
- Charts    
    - Progress Charts
        - Tree
            - Formatting
                - Chart name
                - Node text wrapping
                - Complete/incomplete colouring
            - Input Styling
            - Select Parent Dropdown
            - Dashboard title should be 
    - Create IntentionAlignment
    - Create services to create chart data, plus required API infrastructure - generic?
    - Eisenhower Matrix
        - filter by parent goal
- workout
    - Exercise (Type)
    - Workout
      - Set
        - Repetition
- Meal Planning
- Habits (Actions -> Habits refactor)
    - 'Habit goals' (maintain x for 10 days, increase y by z amount) are Habit Milestones, separate aggregate
