using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public enum State
{
    PATROL,
    ATTACK,
    RUN
}

public class EnemyController : MonoBehaviour
{
    public Animator anim;
    public NavMeshAgent nav;

    private State inerState;

    public float walk_speed = 0.5f;
    public float run_speed = 4f;
    public float spot_range = 40f;
    public float health = 100f;
    public float attack_range = 0.2f;
    public float attack_damage = 5f;
    public float attack_delay = 2f;
    public float wanderRadius = 50f;
    public float wanderTimer = 20f;
    private float timer;
    private float patrol_Timer;
    private float attack_Timer;
    private float patrol_For_This_Time = 0;

    private Transform target;

    // Start is called before the first frame update
    void Start()
    {
        inerState = State.PATROL;
        timer = wanderTimer;
        target = GameObject.FindWithTag("Player").transform;
    }

    // Update is called once per frame
    void Update()
    {
        if (inerState == State.PATROL)
        {
            Patrol();
        }

        if (inerState == State.RUN)
        {
            Chase();
        }

        if (inerState == State.ATTACK)
        {
            Attack();
        }
        timer += Time.deltaTime;

        //if (timer >= wanderTimer)
        //{
        //    Vector3 newPos = GetRandDir();
        //    nav.SetDestination(newPos);
        //    nav.isStopped = false;
        //    Walk(true);
        //    timer = 0;
        //}
        //SearchTarget();
    }

    void Patrol()
    {

        // tell nav agent that he can move
        nav.isStopped = false;
        nav.speed = walk_speed;

        // add to the patrol timer
        patrol_Timer += Time.deltaTime;

        if (patrol_Timer > 40f)
        {

            GetRandDir();
            patrol_Timer = 0f;

        }

        if (nav.velocity.sqrMagnitude > 0)
        {

            Walk(true);

        }
        else
        {

            Walk(false);

        }


        if (Vector3.Distance(transform.position, target.position) <= spot_range)
        {

            Walk(false);

            inerState = State.RUN;

        }


    }

    void Chase()
    {

        // enable the agent to move again
        nav.isStopped = false;
        nav.speed = run_speed;

        // set the player's position as the destination
        // because we are chasing(running towards) the player
        nav.SetDestination(target.position);

        if (nav.velocity.sqrMagnitude > 0)
        {

            Run(true);

        }
        else
        {

            Run(false);

        }

        // if the distance between enemy and player is less than attack distance
        if (Vector3.Distance(transform.position, target.position) <= attack_range)
        {

            // stop the animations
            Run(false);
            Walk(false);
            inerState = State.ATTACK;


        }
        else if (Vector3.Distance(transform.position, target.position) > spot_range)
        {
            // player run away from enemy

            // stop running
            Run(false);

            inerState = State.PATROL;

            // reset the patrol timer so that the function
            // can calculate the new patrol destination right away
            patrol_Timer = patrol_For_This_Time;


        } // else

    } // chase

    void Attack()
    {

        nav.velocity = Vector3.zero;
        nav.isStopped = true;

        attack_Timer += Time.deltaTime;

        if (attack_Timer > attack_delay)
        {

            Attack_anim();

            attack_Timer = 0f;

        }

        if (Vector3.Distance(transform.position, target.position) >
           attack_range)
        {

            inerState = State.RUN;

        }


    }

    void SearchTarget()
    {
        if (Vector3.Distance(transform.position, target.position) < spot_range)
        {
            Walk(false);
            Run(true);
            inerState = State.RUN;
            nav.isStopped = false;
            Vector3 newPos = SamplePos(target.position, wanderRadius);
            nav.SetDestination(newPos);
            if (Vector3.Distance(transform.position, target.position) < attack_range)
            {
                Run(false);
                Walk(true);
                nav.isStopped = true;
                Attack();
            }
        }
    }

    public void takeDamage(float damage)
    {
        health -= damage;
        if (health <= 0)
        {
            Die(true);
        }
        else
        {
            nav.isStopped = true;
        }
    }

    Vector3 SamplePos(Vector3 Direction, float wanderRadius)
    {
        NavMeshHit navHit;

        NavMesh.SamplePosition(Direction, out navHit, wanderRadius, -1);

        return navHit.position;
    }

    Vector3 GetRandDir()
    {
        Vector3 randomDirection = UnityEngine.Random.insideUnitSphere * wanderRadius;

        randomDirection += transform.position;

        return SamplePos(randomDirection, wanderRadius);
    }

    public void Walk(bool walk)
    {
        anim.SetBool("Walk", walk);
    }
    public void Run(bool run)
    {
        anim.SetBool("Run", run);
    }
    public void Attack_anim()
    {
        anim.SetTrigger("Attack");
    }
    public void Die(bool Die)
    {
        // anim.SetBool("Die", Die);
    }
}
